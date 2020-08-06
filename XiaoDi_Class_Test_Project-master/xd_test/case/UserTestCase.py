# -*- coding:UTF-8 -*-
import unittest
# from xd_test.case.xin import UserTestCase1
from xd_test.util.RequestUtil import RequestUtil

host = 'https://api.xdclass.net'


class UserTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass在所有的测试用例执行之前，只执行一次==============")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass在所有的测试用例执行之后，只执行一次==============")

    # 测试用例必须使用text开头
    def testCase1(self):
        print("test Case1")

    @unittest.skip("跳过testCase2=========================================")
    def testCase2(self):
        print("test Case2")
        # self.assertEqual(1,1)

    def testCase3(self):
        print("test Case3")

    def testLogin(self):
        """
        用户登录
        :return:
        """
        request = RequestUtil()
        url = host + '/pub/api/v1/web/web_login'
        data = {"phone": 13840453509, "pwd": "wrx516615"}
        response = request.request(url, 'post', param=data, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response['code'], 0, "登录接口测试失败")


if __name__ == '__main__':
    # 简单执行程序
    # verbosity参数取值1，2，3，默认为1
    # unittest.main(verbosity=2)

    # 使用测试套件 TestSuite
    suite = unittest.TestSuite()

    # 逐个添加测试用例
    # suite.addTest(UserTestCase("testCase1"))
    # suite.addTest(UserTestCase("testCase3"))
    # suite.addTest(UserTestCase("testCase2"))
    # suite.addTest(UserTestCase1("testCase3"))

    # 批量添加测试用例
    # suite.addTests([UserTestCase("testCase1"), UserTestCase("testCase3"), UserTestCase1("testCase3")])

    # 使用TestLoader多个文件测试用例批量加载   用例执行没有指定顺序
    loader = unittest.TestLoader()
    # 加载导入某个模块的全部用例
    # suite.addTests(loader.loadTestsFromTestCase(UserTestCase1))
    suite.addTests(loader.loadTestsFromTestCase(UserTestCase))

    # 使用Discover多个文件测试用例批量加载  一般放在主运行文件里

    # 生成文本测试运行器并执行
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
