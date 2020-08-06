# -*- coding:UTF-8 -*-
import unittest


class UserTestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass在所有的测试用例执行之前，只执行一次==============")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass在所有的测试用例执行之后，只执行一次==============")

    def testCase1(self):
        print("UserTestCase1 test Case1")

    @unittest.skip("跳过testCase2=========================================")
    def testCase2(self):
        print("UserTestCase1 test Case2")
        # self.assertEqual(1,1)

    def testCase3(self):
        print("UserTestCase1 test Case3")


if __name__ == '__main__':
    # 简单执行程序
    # verbosity参数取值1，2，3，默认为1
    unittest.main(verbosity=2)