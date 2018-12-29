#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Changrui"
__pkuid__  = "1800011758"
__email__  = "706771104@qq.com"
"""


import sys
from urllib.request import urlopen

def wcount(passage,topn=10):
    l = [",",".","?",":","!",";"]
    passage=passage.lower()
    for i in l:
        passage=passage.replace( i ,"")
    # 去除标点符号
    list1=passage.split()
    #以空格分开各个单词
    list_withoutspace=[]
    list_element=[]
    dic1={}
    for i in list1:
        if i!="":
            list_withoutspace.append(i)
    #得到去除空格的列表
    for i in list_withoutspace:
        if i not in list_element:
            list_element.append(i)
    #得到含有所有种单词各一个的列表
    for i in list_element:
        dic1[i]=list_withoutspace.count(i)
    #计数并创建字典
    list_result=sorted(dic1.items(),key=lambda x:x[1],reverse=True)
    #按单词数目降序排列
    if int(topn)>len(list_result):
        topn=str(len(list_result))
    #如果输入的数目大于单词种类的总数则输出所有单词
    for i in range(int(topn)):
        print(list_result[i])

def main():
    doc = urlopen(sys.argv[1])
    docstr = doc.read()
    doc.close()
    passage = docstr.decode()
    if len(sys.argv) == 2:
        wcount(passage)
    elif len(sys.argv) == 3:
        wcount(passage,sys.argv[2])
        
if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        main()