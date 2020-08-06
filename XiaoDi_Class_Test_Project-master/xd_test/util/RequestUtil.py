import requests


"""
HTTP工具类的封装
"""
class RequestUtil:
    def __init__(self):
        pass

    def request(self, url, method, headers=None, param=None, content_type=None):
        """
        通用请求工具类
        :param url:
        :param method:
        :param hesders:
        :param param:
        :param content_type:
        :return:
        """
        try:
            if method == 'get':
                result = requests.get(url=url, params=param, headers=headers).json()
                return result
            elif method == 'post':
                if content_type == 'application/json':
                    result = requests.post(url=url, json=param, headers=headers).json()
                    return result
                else:
                    result = requests.post(url=url, data=param, headers=headers).json()
                    return result
            else:
                print("http method not allow !")
        except Exception as e:
            print("http请求报错：{0}".format(e))


if __name__ == '__main__':
    # 测试get请求
    # url = "https://api.xdclass.net/pub/api/v1/web/all_category"
    # r = RequestUtil();
    # result = r.request(url, 'get')
    # print(result)
    # 测试post请求
    url = "https://api.xdclass.net/pub/api/v1/web/web_login"
    r = RequestUtil()
    data = {"phone": 13840453509, "pwd": "wrx516615"}
    result = r.request(url, "post", param=data, content_type="application/x-www-form-urlencoded")
    print(result)
