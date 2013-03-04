#!/usr/bin/env python

from setuptools import setup

setup(
    name='hutil',
    version='0.1',
    author='Daegeun Kim',
    author_email='dgkim84@gmail.com',
    url='https://github.com/dgkim84/hutil',
    long_description=open('README.md').read(),
    packages=['hutil'],
    scripts = ['bin/hutil'],
    include_package_data = True,
    install_requires=['BeautifulSoup', 'PyYAML'],
    classifiers=[
    ],
)

