#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read().replace('# Changelog', '')

requirements = [
    'demands==1.0.6',
    'property-caching==1.0.3',
    'querylist==0.2.0',
]

test_requirements = [
    'unittest2==1.0.1',
]

setup(
    name='authoritylabs-python',
    version='0.1.0',
    description="Python client for Authority Labs' Partner API",
    long_description=readme + '\n\n' + changelog,
    author="Yola",
    author_email='engineers@yola.com',
    url='https://github.com/yola/authoritylabs-python',
    packages=find_packages(exclude=('tests*',)),
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='authoritylabs development',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
