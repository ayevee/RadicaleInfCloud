#!/usr/bin/env python3

import os

from setuptools import setup

VERSION = "3.0.0"

os.chdir("radicale_infcloud")
web_data = sum(([os.path.join(root, f) for f in files
                 if not f.startswith(".") and not f.endswith("~")]
                for root, _, files in os.walk("web")), [])
os.chdir(os.pardir)

setup(
    name="Radicale_InfCloud",
    version=VERSION,
    description="InfCloud for Radicale",
    author="ayevee (forked from Unrud)",
    url="https://github.com/ayevee/RadicaleInfCloud",
    license="GNU AGPL v3",
    platforms="Any",
    packages=["radicale_infcloud"],
    package_data={"radicale_infcloud": web_data},
    install_requires=["radicale>=3.0.0"])
