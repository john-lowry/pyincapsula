#!/usr/bin/env python

from setuptools import setup

setup(
    name='incapsula', 
    version='0.02',
    author="John Lowry",
    author_email="johnlowry@gmail.com"
    description=("A python module for using the Incapsula API"),
    keywords="WAF Incapsula",
    packages=['incapsula',],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: Other/Proprietary License",
        "Topic :: Security",
    ],
)

