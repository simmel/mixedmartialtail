#!/usr/bin/env python3
# vim: set fileencoding=utf-8
'''
mixedmartialtail: a warlike approach to tailing logs with mixed formats

Copyright 2016-, Simon Lundström <simmel@soy.se>.
Licensed under the ISC license.
'''

import sys
from setuptools import setup

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
        'console_scripts': [
            'mmt=mixedmartialtail:main'
        ]
    },
    extras_require={
        'dev': [
            'check-manifest',
        ],
        'test': [
            'check-manifest',
            'pytest',
        ],
    },
)