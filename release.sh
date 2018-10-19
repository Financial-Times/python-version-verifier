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

echo "[pip] v10.0.1 installing..."
pip -q install --upgrade pip==10.0.1
echo "[pip] aws_composer_general's python_release installing..."
pip -q install \
    -U \
    -e \
    "git+ssh://git@github.com/Financial-Times/aws-composer-pipeline-scripts-general.git@master#egg=aws_composer_general[python_release]" \
    -r requirements.txt \
    --process-dependency-links

# CLEAN DISTRIBUTION
rm -rf dist/ build/ "$(python3 setup.py --name).egg-info/"

# RUN_TESTS
composer run-tests --coverage --cov_dir="$(python3 setup.py --name)" tests
rm -f setup.cfg  # file only created to run unittests
xmllint --format tests.xml --output tests.linted.xml && mv tests.linted.xml tests.xml

# PACKAGE
# BUMP VERSION
VERSION_FILE=$(python3 setup.py --name)/__init__.py
if grep -q ^__version__ "${VERSION_FILE}"; then
    NEXT_VERSION=$(git semver --next-patch)
    sed -i'' -e 's!^__version__ = .*$!__version__ = "'"$NEXT_VERSION"'"!' "${VERSION_FILE}"
else
    echo "__version__ not found in $VERSION_FILE"
    exit 9
fi

# UPDATE CHANGELOG
#touch CHANGELOG.md
#echo "[$NEXT_VERSION]" > new-CHANGELOG.md
#git log "$(git semver)..HEAD" --no-merges --format="%an, %aD%n    %s%n" >> new-CHANGELOG.md
#cat CHANGELOG.md >> new-CHANGELOG.md
#mv new-CHANGELOG.md CHANGELOG.md
./changelog.sh

git commit -m "Version $NEXT_VERSION" "${VERSION_FILE}" CHANGELOG.md
git push

# Create Github Release for Version
generate_post_data() {
  cat <<EOF
{
  "tag_name": "$NEXT_VERSION",
  "target_commitish": "master",
  "name": "$NEXT_VERSION",
  "body": "Version $NEXT_VERSION",
  "draft": false,
  "prerelease": false
}
EOF
}
repo_full_name=$(git config --get remote.origin.url | sed 's/.*://;s/.git$//')
token=$(composer decrypt -n github-token-gocd-utilities-new-repo)
curl -s \
    --data "$(generate_post_data)" \
    "https://api.github.com/repos/$repo_full_name/releases?access_token=${token}"

# PACKAGE
python3 setup.py sdist
python3 setup.py bdist_wheel --universal

# CHECK
echo "twine check"
twine check dist/*

# DEPLOY
echo twine upload --repository-url "https://ce-publish-nexus:${CE_PUBLISH_NEXUS}@nexus.in.ft.com/repository/python-releases/" dist/*
twine upload --verbose -u ce-publish-nexus -p "${CE_PUBLISH_NEXUS}" --repository-url "https://nexus.in.ft.com/repository/python-releases/" dist/*
