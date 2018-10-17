#!/usr/bin/env bash

# this is used by the aws-composer-tools pipeline to test / check coverage

set -e
# SETUP
if [ -d venv ]; then
    rm -rf venv
fi

virtualenv -p python3.6 venv >/dev/null 2>&1
# shellcheck source=/dev/null
source venv/bin/activate

pip install --upgrade pip==10.0.1
pip install \
    -U \
    -e \
    "git+ssh://git@github.com/Financial-Times/aws-composer-pipeline-scripts-general.git@master#egg=aws_composer_general[python_release]" \
    -r requirements.txt \
    --process-dependency-links

# CLEAN DISTRIBUTION
rm -rf dist/ build/ "$(python3 setup.py --name).egg-info/"

# RUN_TESTS
composer run-tests --coverage --cov_dir=python_version_verifier tests
xmllint --format tests.xml --output tests.linted.xml && mv tests.linted.xml tests.xml

# PACKAGE
# BUMP VERSION
VERSION_FILE=$(python3 setup.py --name)/__init__.py
if grep -q ^__version__ "${VERSION_FILE}"; then
    git semver --next-patch >/dev/null 2>/dev/null
    if [ "$?" -eq "1" ]; then
        # create initial tag
        git tag -am 0.0.1 0.0.1
        git push origin --tags
    fi
    NEXT_VERSION=$(git semver --next-patch)
    sed -i '' -e 's!^__version__ = .*$!__version__ = "'"$NEXT_VERSION"'"!' "${VERSION_FILE}"
else
    echo "__version__ not found in $VERSION_FILE"
    exit 9
fi
# UPDATE CHANGELOG
touch CHANGELOG.md
echo "[$NEXT_VERSION]" > new-CHANGELOG.md
git log "$(git semver)..HEAD" --no-merges --format="%an, %aD%n    %s%n" >> new-CHANGELOG.md
cat CHANGELOG.md >> new-CHANGELOG.md
mv new-CHANGELOG.md CHANGELOG.md

git commit -m "Version $NEXT_VERSION" "${VERSION_FILE}" CHANGELOG.md
git push

# Tag Release/Tag and push back to GitHub
git tag -am "${NEXT_VERSION}" "${NEXT_VERSION}"
git push origin --tags

# PACKAGE
python3 setup.py sdist bdist_wheel

# CHECK
twine check dist/*

# DEPLOY
twine upload --repository-url "https://ce-publish-nexus:${CE_PUBLISH_NEXUS}@nexus.in.ft.com/repository/python-releases/" dist/*
