#!/usr/bin/env python

from setuptools import setup

setup(
    name="mathutils",
    version="0.0.1",
    author="NFQ Solutions",
    author_email="some@email.com",
    packages=[
        'nfq.mathutils',
        ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
    )