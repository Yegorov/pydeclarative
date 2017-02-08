#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

required = [

]

vars = {}
with open((path.join(here, 'pydeclarative', '__about__.py'))) as fp:
    exec(fp.read(), vars)

setup(
    name='pydeclarative',
    version=vars['__version__'],
    description='Declarative style in Python.',
    long_description=long_description,
    author='Yegorov A.',
    author_email='yegorov0725@yandex.ru',
    url='https://github.com/yegorov/pydeclarative',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=required,
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='declarative function loop chain',
)