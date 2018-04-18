#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ziqi on 2018/4/18
# This the setup.py script in the PythonSkeleton project


# coding=utf-8
from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="PythonSkeleton",
    version="0.0.1",
    description="python skeleton demo",
    long_description=open("README.md", encoding='utf-8').read(),
    author="ziqi",
    author_email="zzq438283168@gmail.com",
    url="",
    license="",
    packages=find_packages(exclude=("tests", "docs", "etc")),
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    test_suite="Tests"
    # entry_points="""
    #     [console_scripts]
    #     python-skeleton=python_skeleton.cli:main
    # """
)
