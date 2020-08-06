# -*- coding:UTF-8 -*-
import unittest
from xd_test.util.RequestUtil import RequestUtil

host = 'https://api.xdclass.net'


class IndexTextCase(unittest.TestCase):
    def testIndexCategoryList(self):
        """
        首页分类列表
        :return:
        """
        request = RequestUtil()
        url = host + "/pub/api/v1/web/all_category"
        reponse = request.request(url, 'get')
        self.assertEqual(reponse['code'], 0, "业务状态不正常")
        self.assertTrue(len(reponse['data']) > 0, "分类列表为空")
    def testIndexVideoCard(self):
        """
        首页视频卡片
        :return:
        """
        request = RequestUtil()
        url = host + "/pub/api/v1/web/index_card"
        reponse = request.request(url, 'get')
        self.assertEqual(reponse['code'], 0, "业务状态不正常")
        self.assertTrue(len(reponse['data']) > 0, "视频卡片为空")
        video_card_list = reponse['data']
        for card in video_card_list:
            self.assertTrue(len(card['title']) > 0, "卡片标题为空 id=:" + str(card['id']))

if __name__ == '__main__':
    unittest.main(verbosity=2)
