#!/usr/bin/env python
# encoding: utf-8
"""
@author: taoxuefeng
@file: PkusegTest.py
@time: 2019/1/11 17:42
@desc:

"""
import pkuseg

seg1 = pkuseg.pkuseg()                   #以默认配置加载模型
text = seg1.cut('我爱北京天安门')        #进行分词
print(text)

lexicon = ['北京大学','北京天安门']      #希望分词时用户词典重的词固定不分开
seg2 = pkuseg.pkuseg(user_dict=lexicon)   # 加载模型，给定用户词典
text = seg2.cut('我爱北京天安门')           #进行分词
print(text)

seg3 = pkuseg.pkuseg(model_name='/Users/taoxuefeng/pkuseg_txt/ctb8')
text = seg3.cut('我爱北京天安门')
print(text)

#对input.txt的文件分词输出到output.txt中，使用默认模型和词典，开20个进程
pkuseg.test('/Users/taoxuefeng/girl_1.txt','/Users/taoxuefeng/pkusegOutput.txt',nthread=20)