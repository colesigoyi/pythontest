{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "对BeautifulSoup进行初步学习"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "from urllib.request import urlopen\n",
    "html = urlopen(\"https://morvanzhou.github.io/static/scraping/basic-structure.html\"\n",
    "              ).read().decode('utf-8')\n",
    "print(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<h1>爬虫测试1</h1>\n",
      "\n",
      " <p>\n",
      "\t\t这是一个在 <a href=\"https://morvanzhou.github.io/\">莫烦Python</a>\n",
      "<a href=\"https://morvanzhou.github.io/tutorials/data-manipulation/scraping/\">爬虫教程</a> 中的简单测试.\n",
      "\t</p>\n"
     ]
    }
   ],
   "source": [
    "soup = BeautifulSoup(html, features='lxml')\n",
    "print(soup.h1)\n",
    "print('\\n',soup.p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " ['https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/data-manipulation/scraping/']\n"
     ]
    }
   ],
   "source": [
    "all_href = soup.find_all('a')\n",
    "all_href = [l['href'] for l in all_href]\n",
    "print('\\n', all_href)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://morvanzhou.github.io/\n",
      "https://morvanzhou.github.io/tutorials/data-manipulation/scraping/\n"
     ]
    }
   ],
   "source": [
    "all_href1 = soup.find_all('a') #和上面的功能等价\n",
    "for l in all_href1:\n",
    "    print(l['href'])"
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
