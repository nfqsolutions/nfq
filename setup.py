#!/usr/bin/env python

from setuptools import setup

setup(
    name="nfq",
    description="NFQ Solutions base package",
    version="0.1.2",
    author="NFQ Solutions",
    author_email="solutions@nfq.es",
    packages=[
        'nfq',
        ],
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    setup_requires=[],
    tests_require=[]
    )
