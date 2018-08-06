#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 1. 导入模块
import urllib.request


# 2. 发送请求 获取响应
url = "https://www.baidu.com"

# 提供请求头
# 创建请求对象
request = urllib.request.Request(
    url=url,
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36"
    }
)


response = urllib.request.urlopen(request)

# 3. 处理数据
with open('01-baidu.html','wb') as f:
    f.write(response.read())