{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<html lang=\"cn\">\n",
      "<head>\n",
      "\t<meta charset=\"UTF-8\">\n",
      "\t<title>爬虫练习 列表 class | 莫烦 Python</title>\n",
      "\t<style>\n",
      "\t.jan {\n",
      "\t\tbackground-color: yellow;\n",
      "\t}\n",
      "\t.feb {\n",
      "\t\tfont-size: 25px;\n",
      "\t}\n",
      "\t.month {\n",
      "\t\tcolor: red;\n",
      "\t}\n",
      "\t</style>\n",
      "</head>\n",
      "\n",
      "<body>\n",
      "\n",
      "<h1>列表 爬虫练习</h1>\n",
      "\n",
      "<p>这是一个在 <a href=\"https://morvanzhou.github.io/\" >莫烦 Python</a> 的 <a href=\"https://morvanzhou.github.io/tutorials/data-manipulation/scraping/\" >爬虫教程</a>\n",
      "\t里无敌简单的网页, 所有的 code 让你一目了然, 清晰无比.</p>\n",
      "\n",
      "<ul>\n",
      "\t<li class=\"month\">一月</li>\n",
      "\t<ul class=\"jan\">\n",
      "\t\t<li>一月一号</li>\n",
      "\t\t<li>一月二号</li>\n",
      "\t\t<li>一月三号</li>\n",
      "\t</ul>\n",
      "\t<li class=\"feb month\">二月</li>\n",
      "\t<li class=\"month\">三月</li>\n",
      "\t<li class=\"month\">四月</li>\n",
      "\t<li class=\"month\">五月</li>\n",
      "</ul>\n",
      "\n",
      "</body>\n",
      "</html>\n"
     ]
    }
   ],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "from urllib.request import urlopen\n",
    "html = urlopen(\"https://morvanzhou.github.io/static/scraping/list.html\"\n",
    "              ).read().decode('utf-8')\n",
    "print(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "一月\n",
      "二月\n",
      "三月\n",
      "四月\n",
      "五月\n"
     ]
    }
   ],
   "source": [
    "soup = BeautifulSoup(html, features='lxml')  #以lxml形式进行对html的解析\n",
    "month = soup.find_all('li',{\"class\":\"month\"})\n",
    "for m in month:\n",
    "    print(m.get_text())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "一月一号\n",
      "一月二号\n",
      "一月三号\n"
     ]
    }
   ],
   "source": [
    "jan = soup.find('ul',{\"class\":\"jan\"})\n",
    "d_jan = jan.find_all('li')\n",
    "for j in d_jan:\n",
    "    print(j.get_text())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
