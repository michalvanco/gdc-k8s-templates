#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2019, GoodData(R) Corporation. All rights reserved

import os
import sys

from setuptools import setup

# Parameters for build
params = {
    'name': '{{cookiecutter.app_name}}',
    'version': '1.0.0',
    'packages': [
        '{{cookiecutter.base_package}}'
    ],
    'url': '{{cookiecutter.target_github_repository}}',
    'license': 'Proprietary',
    'author': 'GoodData Corporation',
    'author_email': '{{cookiecutter.maintainer}}',
    'description': '{{cookiecutter.description}}',
    'entry_points': {
        'console_scripts': [
            '{{cookiecutter.app_name}} = {{cookiecutter.base_package}}.main:main',
        ],
    },
    'long_description': '{{cookiecutter.description}}',
    'install_requires': ['PyYAML==5.1', 'prometheus_client==0.6.0'],
    'zip_safe': False,
    'include_package_data': True
}

try:
    action = sys.argv[1]
except IndexError:
    action = None

if action == 'test':
    raise Exception('Unsupported, use tox instead!')
elif action == 'clean':
    # Remove MANIFEST file
    print("Cleaning MANIFEST..")
    try:
        os.unlink('MANIFEST')
    except OSError as e:
        if e.errno == 2:
            # file does not exist, continue
            pass
        else:
            raise

    # Remove dist and build directories
    for directory in ['dist', 'build']:
        print("Cleaning %s.." % directory)
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        try:
            os.rmdir(directory)
        except OSError as e:
            if e.errno == 2:
                # file does not exist, continue
                pass
            else:
                raise
else:
    setup(**params)
