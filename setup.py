from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "iedb",
    version = "0.0.2",
    author = "Matt Femia",
    description = "Python SDK for IEDB Tools API. Full details can be found at \
    http://tools.iedb.org/main/tools-api/",
    license = "MIT",
    keywords = "iedb mhc mhc-binding t-cell epitope mhc-i mhc-ii hla",
    url = "http://packages.python.org/iedb",
    packages = ['iedb', 'tests'],
    install_requires=['pandas>=1.0.0', 'requests>=2.22.0'],
    python_requires = '>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Operating System :: OS Independent"
    ],
)