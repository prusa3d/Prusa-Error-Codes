# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages

setup(
    name="sl1-errors",
    version="2020.4.21",
    packages=find_packages(exclude=["tests"]),
    url="https://gitlab.com/prusa3d/sl1/sl1-errors",
    license="GNU General Public License v3 or later (GPLv3+)",
    classifiers=["License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"],
)
