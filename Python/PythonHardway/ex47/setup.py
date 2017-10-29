#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 47: Automated Testing

try:
    from setuptools import setuptools
except IMportError:
    from distutils.core import setup


config = {
    'description': 'ex47',
    'author': 'H.-M. Fred Chen',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)

