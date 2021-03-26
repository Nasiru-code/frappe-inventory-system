# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in inventory/__init__.py
from inventory import __version__ as version

setup(
	name='inventory',
	version=version,
	description='inventory management system',
	author='nacwc',
	author_email='akingbolahan12@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
