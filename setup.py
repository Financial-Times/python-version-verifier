import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_version_verifier",
    version="0.0.1",
    author="Financial Times - Cloud Enablement Team",
    author_email="cloudenablement@ft.com",
    description="A python 3 verions checking library for python functions",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
