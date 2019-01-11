
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
#请求头信息
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
#封装信息
url = 'https://car.autohome.com.cn/photolist/series/588/p{}/'
bigurl = 'https://car.autohome.com.cn/photo/{}'
i = 1
for x in range(1, 5):
    newsurl = url.format(x)
    res = requests.get(newsurl, headers = header).text # 发送HTTP请求
    # print(res)
    num = re.findall('<li id="li.+?" ><a href="/photo/series/(.+?)"',res,re.S)
    # print(num)
     
    for nums in num:
        newsurl = bigurl.format(nums)
        # print(newsurl)
        bigres = requests.get(newsurl, headers = header).text # 发送HTTP请求
        # print(res)
        src = re.findall('id="img" src="//car(.+?).jpg"',bigres,re.S)
        # print(src)
        for each in src:
        # print(each)
            try:
                pic = requests.get("https://car" + each + ".jpg", timeout=50)
                print("第", i, "张下载完成")
            except requests.exceptions.ConnectionError:
                print('错误：当前图片无法啊下载。')
                continue

            string = 'big_auto\\' + str(i) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            i += 1


