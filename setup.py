import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
with open("README.md", "r") as fh:
    README = fh.read()

# This call to setup() does all the work
setup(
    name="IngestFailer",
    version="1.0.0",
    description="Small GUI utility to force a callback timeout for the British Library's AVSIP Tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cjweaver/IngestFailer",
    author="Chris Weaver",
    author_email="christopher.weaver@bl.uk",
    license="GPLv3",
    classifiers=[
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=["requests", "pypiwin32", "pywin32-ctypes"],
    entry_points={
        "console_scripts": [
            "IngestFailer=ingestfailer.__main__:main",
        ]
    },
)