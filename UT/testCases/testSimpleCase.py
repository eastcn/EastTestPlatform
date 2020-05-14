"""
file: testSimpleCase
date: 2020.05.09
author: hefeng
function:
"""
import sys
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

    @unittest.skip("this is skipped")  # 直接跳过
    def test_skip(self):
        print("skip test")

    @unittest.skipIf(True, "this is true")  # 条件判断跳过
    def test_skip_if(self):
        print("this will skipped")

    @unittest.skipUnless(sys.platform.startswith("dar"), "需要mac才能运行")  # 满足条件时可运行，不满足则跳过
    def test_skip_unless(self):
        print("this is mac")

    @unittest.expectedFailure  # 函数断言失败时，测试通过
    def test_expect_fail(self):
        print("失败")


if __name__ == '__main__':
    unittest.main()
