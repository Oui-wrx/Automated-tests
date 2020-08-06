# -*- coding:UTF-8 -*-
import unittest
import os


def load_all_case():
    """
    加载全部测试用例
    :return:
    """
    # 该文件所在的目录
    # print(os.getcwd())
    case_path = os.path.join(os.getcwd(), "case")   # 有时候使用../case
    # 测试用例所在的目录
    # print(case_path)
    # 记载指定目录的全部测试用例
    disCase = unittest.defaultTestLoader.discover(case_path, pattern="*.py", top_level_dir=None)
    # 找到的所有测试用例
    # print(disCase)
    return disCase


if __name__ == '__main__':
    # 执行run发现的测试用例
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_all_case())
