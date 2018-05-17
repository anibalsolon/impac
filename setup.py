#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

with open('impac/requirements.txt') as f:
    required = f.read().splitlines()

required += ["ramp-workflow"]

links = [
    "git+https://github.com/paris-saclay-cds/ramp-workflow.git#egg=ramp-workflow-1.0"
]

setup(name = "impac",
      version = "1.0.0",
      long_description = "",
      packages=find_packages("impac"),
      package_data = {
          "impac": ["data/*"],
      },
      include_package_data=True,
      install_requires=required,
      dependency_links=links,
      license = "MIT"
      )