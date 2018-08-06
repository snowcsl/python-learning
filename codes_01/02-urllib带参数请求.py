#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 1. 导入模块
import urllib.request
import urllib.parse

wd = input("请输入查询内容:")

# 2. 发送请求 获取响应
# url 转义
# 为什么要 url 转义
# 非 ascii 数据都要转义

url = "https://www.baidu.com/s?wd="

# 提供请求头
# 创建请求对象
request = urllib.request.Request(
    url=url + urllib.parse.quote(wd),  # urllib.parse.quote 把 url 进行转义
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
)

response = urllib.request.urlopen(request)

'''
1. 二进制数据 和 字符串 数据之间区别
2. decode 和 encode
3. utf-8 是什么 unicode 是什么

'''

# python内存中字符串计算 所有都是使用 unicode

# 3. 处理数据
# wb 表示 二进制写入
data = response.read()
# w 表写入字符串
# data(二进制) 转成 字符串
# 把二进制 通过 UTF-8 解码成 unicode, 除了 UTF-8 / UTF-16 /UTF-32 / gbk / gb2312
string = data.decode('utf-8')

# with open('01-baidu.html','wb') as f:
#     f.write(response.read())


# data = string.encode('utf-8')
# 如果写入是一个 w 其实内部操作 字符串 转 二进制 写入硬盘
# unicode 数据 编码成 UTF-8
with open('01-baidu.html', 'w', encoding='utf-8') as f:
    f.write(string)
import re