#!/usr/bin/env python

from setuptools import setup

setup(
    name='incapsula', 
    version='0.02',
    author='John Lowry',
    author_email='johnlowry@gmail.com',
    description='A python module for using the Incapsula API',
    url='https://github.com/j-lowry/pyincapsula',
    license='GPL v2.0',
    keywords="WAF Incapsula",
    packages=['incapsula',],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Security",
    ],
    install_requires=[
        'requests',
    ],
)

