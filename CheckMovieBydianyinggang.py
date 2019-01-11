#!/usr/bin/env python
# encoding: utf-8
"""
@author: taoxuefeng
@file: CheckMovieBydianyinggang.py
@time: 2019/1/12 00:08
@desc:实现对电影港每天的更新资源的查询，主要查询每一天的电影更新情况，将文件类型
改为.command可实现双击直接运行，并将结果显示在终端

"""
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import datetime

def getUrl():
    html = urlopen("http://www.dygang.net/"
                  ).read().decode('gb2312')
    soup = BeautifulSoup(html, features='lxml')  #以lxml形式进行对html的解析

    all_url_text = soup.find('div',{"id":"tab1_div_0"}) #和上面的功能等价

    all_url = all_url_text.find_all('a',{"class":"c2"})
    count = 0
    today=datetime.date.today()
    print(today,"电影资源：")
    for url in all_url:
        count += 1
        print(count,":",url.get_text(),'       ',url['href'])

if __name__ == '__main__':
    getUrl()