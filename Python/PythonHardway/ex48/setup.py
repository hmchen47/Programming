#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 46: A Project Skeleton

try:
    from setuptools import setuptools
except IMportError:
    from distutils.core import setup


config = {
    'descition': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)

