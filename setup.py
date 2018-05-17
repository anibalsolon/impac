#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages

with open('impac/requirements.txt') as f:
    required = f.read().splitlines()

required += ["ramp-workflow"]

links = [
    "git+https://github.com/paris-saclay-cds/ramp-workflow.git#egg=ramp-workflow-1.0"
]


def touch(fname, times=None):
    fhandle = open(fname, 'a')
    try:
        os.utime(fname, times)
    finally:
        fhandle.close()


touch("impac/__init__.py")
touch("impac/preprocessing/__init__.py")
touch("impac/submissions/combine_anatomy_functional/__init__.py")
touch("impac/submissions/starting_kit/__init__.py")
touch("impac/submissions/starting_kit_anatomy/__init__.py")
touch("impac/submissions/starting_kit_functional/__init__.py")

setup(name = "impac",
      version = "1.0.0",
      long_description = "",
      packages=find_packages("."),
    #   package_data = {
    #       "impac": ["data/*"],
    #   },
    #   include_package_data=True,
      install_requires=required,
      dependency_links=links,
      license = "MIT"
      )