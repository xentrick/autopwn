#!/usr/bin/env python
# coding: utf-8

import re
from os import path
from setuptools import find_packages, setup

PACKAGE_NAME = "autopwn"

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="Autopwn bot for monitoring vulnerable hosts (CTF)",
    url="https://github.com/xentrick/autopwn",
    license="",
    author='Nick Mavis',
    author_email='nmavis@cisco.com',
    packages=find_packages(exclude={"tests", "tests.*"}),
    install_requires=requirements,
    entry_points={
        "console_scripts": ['autopwn = bin/btv']
        },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.7',
    ]
)
