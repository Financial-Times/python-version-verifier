"""Python Version Verifier Package setup."""
import setuptools
import python_version_verifier

setuptools.setup(
    name=python_version_verifier.__title__,
    version=python_version_verifier.__version__,
    author=python_version_verifier.__author__,
    author_email=python_version_verifier.__email__,
    description=python_version_verifier.__summary__,
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    license=python_version_verifier.__license__,
    url=python_version_verifier.__uri__,
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
