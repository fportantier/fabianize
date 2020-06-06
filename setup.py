#!/usr/bin/env python3

import os
import sys
import glob

from pathlib import Path
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

entries = [
    'fabianize = fabianize.cmd_fabianize:cmd_fabianize'
]

setup(
    name='fabianize',
    version='0.0.1',
    description='Fabianization Tool',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Fabian Martinez Portantier',
    author_email='fabian@portantier.com',
    url='https://github.com/fportantier/fabianize',
    license='BSD 3-clause',
    install_requires=[
        'click',
    ],
    tests_require=[
        'pytest',
        'pytest-runner',
    ],
    entry_points={
        'console_scripts': entries,
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.8",
    ],
    packages=['fabianize'],
    include_package_data=True,
    keywords=['security'],
    zip_safe=False,
    test_suite='py.test',
)
