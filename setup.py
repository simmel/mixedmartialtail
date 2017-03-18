#!/usr/bin/env python3
# vim: set fileencoding=utf-8
'''
mixedmartialtail: a warlike approach to tailing logs with mixed formats

Copyright 2016-, Simon Lundström <simmel@soy.se>.
Licensed under the ISC license.
'''

import sys
from setuptools import setup, find_packages

version = "1.0.0"

setup(
    name="mixedmartialtail",
    version=version,
    description="a warlike approach to tailing logs with mixed formats",
    long_description=open("README.md").read(),
    author="Simon Lundström",
    author_email="simmel@soy.se",
    url="https://github.com/simmel/mixedmartialtail",
    license="ISC license",
    entry_points={
        'mixedmartialtail.plugins.input': [
            'cat = mixedmartialtail.plugins.input.cat',
            'json = mixedmartialtail.plugins.input.json',
        ],
        'console_scripts': [
            'mmt=mixedmartialtail:main'
        ]
    },
    install_requires=open('requirements.txt').readlines(),
    extras_require={
        'dev': [
            'check-manifest',
        ],
        'test': [
            'check-manifest',
            'pytest',
            'pytest-benchmark',
            'tox',
        ],
    },
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
