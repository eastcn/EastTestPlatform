"""
file: testSimpleCase
date: 2020.05.09
author: hefeng
function:
"""
import unittest


class TestSimpleCase(unittest.TestCase):
    def setUp(self) -> None:
        print("this is setUp....")

    def tearDown(self) -> None:
        print("this is tearDown")

    def test_one_add_one(self):
        print("this is simple case run:\n 1+1 = 2")
        a = 1 + 1
        self.assertEqual(a, 2)

    def test_str_equal(self):
        print("test hello world not equal Hello World")
        self.assertEqual("hello world", "Hello World")

    def test_bigger(self):
        print("test assert bigger")
        self.assertGreater(3, 2)

    def test_is_instance(self):
        print("test is instance")
        self.assertIsInstance(1, int)


if __name__ == '__main__':
    unittest.main()
