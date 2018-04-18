#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ziqi on 2018/4/18
# This the test_MathDemo script in the PythonSkeleton project


import unittest
from PythonSkeleton.MathDemo import MathDemo


class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once too.")

    def setUp(self):
        print("do something before test.Prepare environment.")

    def tearDown(self):
        print("do something after test.Clean up.")

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, MathDemo.add(1, 2))
        self.assertNotEqual(3, MathDemo.add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, MathDemo.minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, MathDemo.multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, MathDemo.divide(6, 3))
        self.assertEqual(2.6, MathDemo.divide(5, 2))


if __name__ == '__main__':

    unittest.main(verbosity=2)


