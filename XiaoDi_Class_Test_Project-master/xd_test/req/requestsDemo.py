# -*- coding:UTF-8 -*-
import requests

# get请求
# reponse = requests.get("https://api.xdclass.net/pub/api/v1/web/all_category")

# get带参请求
# data = {"video_id": 54}
# https://api.xdclass.net/pub/api/v1/web/video_detail?video_id=53
# reponse = requests.get("https://api.xdclass.net/pub/api/v1/web/video_detail", data)

# post带参请求
# data = {"phone": "13840453509", "pwd": "wrx5166158"}
# reponse = requests.post("https://api.xdclass.net/pub/api/v1/web/web_login", data=data)

# 注意点： post提交⽅式有两个传参⽅式，针对不同的content-type, 务必要指定接⼝是哪个类型，表单提交还是json提交
# Content-Type: application/x-www-formurlencoded
# requests.post("url", data=data)
# Content-Type: application/json
# requests.post("url", json=data)

# 使用token查看对应的信息 get请求
# headers = {"token": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTkuanBlZyIsImlkIjo2NzUxODcsIm5hbWUiOiJPdWkiLCJpYXQiOjE1OTYzMDEyNDUsImV4cCI6MTU5NjkwNjA0NX0.boLKd5RRcxCNmpslTbGHhhPscWFE4B_MWUH8C8tNK_Q"}
# reponse = requests.get("https://api.xdclass.net/pub/api/v1/web/user_info",headers=headers)

# 使用token提交信息 post请求
# headers = {"token": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTkuanBlZyIsImlkIjo2NzUxODcsIm5hbWUiOiJPdWkiLCJpYXQiOjE1OTYzMDEyNDUsImV4cCI6MTU5NjkwNjA0NX0.boLKd5RRcxCNmpslTbGHhhPscWFE4B_MWUH8C8tNK_Q"}
# reponse = requests.post("https://api.xdclass.net/user/api/v1/favorite/save", data={"video_id": 42}, headers=headers)

# 响应http状态码
# print(reponse.status_code)

# 响应文本
# print(reponse.text)

# 响应二进制流，一般用于图片
# print(reponse.content)

# 响应JSON
# print(reponse.json())
