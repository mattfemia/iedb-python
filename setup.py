from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "iedb",
    version = "0.0.1",
    author = "Matt Femia",
    description = "Python SDK for IEDB Tools API. Full details can be found at \
    http://tools.iedb.org/main/tools-api/",
    license = "MIT",
    keywords = "iedb mhc mhc-binding t-cell epitope mhc-i mhc-ii hla",
    url = "http://packages.python.org/iedb",
    packages = ['iedb', 'tests'],
    install_requires=['pandas>=1.0.0', 'requests>=2.22.0'],
    python_requires = '>=3.6',
    long_description = 'Python SDK for IEDB Tools API. Includes API support \
    for the following tools: MHC-I and MHC-II binding, MHC-I processing and \
    MHC-NP predictions for T-cell epitopes.',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Operating System :: OS Independent"
    ],
)