"""
file: demoSuite
date: 2020.05.14
author: hefeng
function: 
"""
import unittest
from UT.testCases.testSimpleCase import TestSimpleCase as case

if __name__ == '__main__':
    # 指定一个TestSuite
    s = unittest.TestSuite()
    # 加入case
    s.addTest(case('test_one_add_one'))

    # 指定一个runner
    runner = unittest.TextTestRunner()
    runner.run(s)
