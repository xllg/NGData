# -*- coding: utf-8 -*-
# @File  : excel2txt.py
# @Author: xllg
# @Date  : 2020/7/30 下午3:40
# @Contact : xllgsc@gmail.com

import pandas as pd
import jieba
import jieba.analyse
from tqdm import tqdm
import collections
from operator import itemgetter

# 读取数据,筛选数据
def loadDataFromExcel(filesrc, usesheet, useclos):
    df = pd.read_excel(filesrc, sheet_name=usesheet,usecols=useclos)
    ds = df[df[df.columns[0]].notnull()] # 选出大类不为空的数据
    da = ds[ds[ds.columns[0]].str.contains('环境卫生')] #选出大类数据
    db = da[da[da.columns[1]].notnull()] # 选出小类不为空的数据
    db = db[db[db.columns[1]].str.contains('环卫作业')] #选出小类数据
    dc = db[db[db.columns[2]].notnull()] # 选出细类不为空的数据
    dc = dc[dc[dc.columns[2]].str.contains('垃圾收运')] #选出细类数据
    data = dc[dc.columns[3]].values #使用来电内容进行分词词频统计
    text = ''.join(data)
    return data, text
# 结巴分词
def jiebaCut(data):
    words = []
    strs = []
    jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
    for i in tqdm(range(len(data))):
        seg_list = jieba.lcut(data[i], use_paddle=True)
        strs.append('/'.join(seg_list))
        words += seg_list
    print(str(len(strs)) + "条来话共计" + str(len(words)) + "个分词被记录！")
    # 词频统计
    word_counts = collections.Counter(words)
    word_counts_sort = sorted(word_counts.items(), key = itemgetter(1),reverse=True)
    return strs, word_counts_sort

def jiebaTFIDF(text, topk):
    keywords = jieba.analyse.extract_tags(text, topK=topk, withWeight=True, allowPOS=())
    return keywords

def write2File(strs, word_counts_sort):
    with open('../data/cut_words.txt', 'w') as f:
        for item in word_counts_sort:
            f.write(str(item) +'\n')

    with open('../data/cut_strs.txt', 'w') as fc:
        for line in strs:
            fc.write(line + '\n')
    print("分词结果写入文件成功!")


if __name__ == '__main__':
    data, text = loadDataFromExcel('../data/6月总表.xlsx', '下级办理', [7, 8, 9, 11])
    keywords = jiebaTFIDF(text, 100)
    for key in keywords:
        print(key)
    # with open('../data/cut_strs.txt', 'w') as fc:
    #     fc.write(text )