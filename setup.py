#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'django-allauth'
]

test_requirements = [
    'django-environ',
    'mock'
]

setup(
    name='allauth_watchdog_id',
    version='0.2.0',
    description="A django-allauth provider for Watchdog ID.",
    long_description=readme + '\n\n' + history,
    author="Adam Dobrawy",
    author_email='naczelnik@jawnosc.tk',
    url='https://github.com/watchdogpolska/allauth_watchdog_id',
    packages=[
        'allauth_watchdog_id',
    ],
    package_dir={'allauth_watchdog_id':
                 'allauth_watchdog_id'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='allauth_watchdog_id',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite="runtests",
    tests_require=test_requirements
)
