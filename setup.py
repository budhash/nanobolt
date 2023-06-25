#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys
import pathlib
from setuptools import setup, find_namespace_packages
import sdist_upip


def list_packages(source_directory: str = ".") -> list:
    packages = list(find_namespace_packages(source_directory, exclude=["venv"]))
    return packages


def get_status_classifier(status: str) -> str:
    status_mapping = {
        "planning": "Development Status :: 1 - Planning",
        "prealpha": "Development Status :: 2 - Pre-Alpha",
        "alpha": "Development Status :: 3 - Alpha",
        "beta": "Development Status :: 4 - Beta",
        "stable": "Development Status :: 5 - Production/Stable",
        "mature": "Development Status :: 6 - Mature",
        "inactive": "Development Status :: 7 - Inactive",
    }
    status = status.lower()
    return status_mapping.get(status, "Development Status :: 4 - Beta")


# https://spdx.org/licenses/
# https://pypi.org/classifiers/
def get_license_info(license: str) -> tuple:
    license_mapping = {
        "apache": ("Apache License 2.0", "License :: OSI Approved :: Apache Software License"),
        "mit": ("MIT", "License :: OSI Approved :: MIT License"),
        "gpl": (
            "GNU General Public License v3.0 or later",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        ),
        "lgpl": (
            "GNU Lesser General Public License v3.0 or later",
            "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        ),
        "agpl": (
            "GNU Affero General Public License v3.0 or later",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        ),
    }
    license = license.lower()
    return license_mapping.get(license, ("", "License :: OSI Approved"))


here = pathlib.Path(__file__).parent.resolve()

# load metadata.json
with open("metadata.json") as json_file:
    metadata = json.load(json_file)

# read the required Python version and convert to tuple
required_python_str = metadata["requirements"]["python"]
required_python_tuple = tuple(map(int, required_python_str.split(".")))

# check current Python version
if sys.version_info < required_python_tuple:
    sys.exit("This package requires Python {} or higher.".format(required_python_str))

# read the requirements.txt file and populate the requirements list
with open(here / "requirements.txt") as f:
    requirements = f.read().splitlines()

# version
exec(open(metadata["project"]["name"] + "/version.py").read())
# license
license_name, license_classifier = get_license_info(metadata["project"]["license"])
# status
status_classifier = get_status_classifier(metadata["project"]["status"])

# Setup
setup(
    name=metadata["project"]["name"],
    version=__version__,  # noqa: F821
    description=metadata["project"]["description"],
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url=metadata["project"]["url"],
    author=metadata["author"]["name"],
    author_email=metadata["author"]["email"],
    license=license_name,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: {}".format(required_python_str.split(".")[0]),
        "Programming Language :: Python :: {}".format(required_python_str),
        "Programming Language :: Python :: Implementation :: MicroPython",
        status_classifier,
        license_classifier,
    ],
    keywords=metadata["project"]["keywords"],
    project_urls={
        "Bug Reports": metadata["project"]["issues"],
        "Source": metadata["project"]["source"],
    },
    cmdclass={"sdist": sdist_upip.sdist},
    packages=list_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=True,
    python_requires=">={}".format(required_python_str),
)
