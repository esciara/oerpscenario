#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
Setup script for oerpscenario.
(largely copied from behave 1.2.4 config.py at
https://github.com/behave/behave/blob/f102ef1b1dca99a1810f03927b3ef7519e7ad6f2/setup.py)

USAGE:
    python setup.py install
    python setup.py behave_test
"""

import sys
import os.path

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, HERE)

from setuptools import find_packages, setup

OERPSCENARIO = os.path.join(HERE, "oerpscenario")
README = os.path.join(HERE, "README.rst")

# -----------------------------------------------------------------------------
# UTILITY:
# -----------------------------------------------------------------------------
def find_packages_by_root_package(where):
    """
    Better than excluding everything that is not needed,
    collect only what is needed.
    """
    root_package = os.path.basename(where)
    packages = [ "%s.%s" % (root_package, sub_package)
                 for sub_package in find_packages(where)]
    packages.insert(0, root_package)
    return packages


# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="oerpscenario",
    version="0.1.0.dev",
    description="DSL to manipulate/test/configure OpenERP/Odoo remotely",
    long_description=open("README.rst").read(),
    author="Camptocamp SA (Nicolas Bessi), Emmanuel Sciara",
    author_email="info@camptocamp.com",
    url="https://github.com/esciara/oerpscenario",
    provides="oerpscenario",
    packages=find_packages_by_root_package(OERPSCENARIO),
    entry_points={
        "console_scripts": [
            "openerp_scenario = oerpscenario.openerp_scenario:main"
        ]
    },
    install_requires=["behave==1.2.4",
                      "erppeek~=1.6.2",
                      "unittest2~=1.1"],
    tests_require=[
        'unittest2~=1.1',
    ],
    test_suite='unittest2.collector',
    license="GPL3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    zip_safe=True,
)