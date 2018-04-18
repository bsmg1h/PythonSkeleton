#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ziqi on 2018/4/18
# This the test_MathDemo script in the PythonSkeleton project


import unittest
from Tests.test_MathDemo import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

