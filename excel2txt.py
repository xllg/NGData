# -*- coding: utf-8 -*-
# @File  : excel2txt.py
# @Author: xllg
# @Date  : 2020/7/30 下午3:40
# @Contact : xllgsc@gmail.com

import pandas as pd
import jieba

# 读取数据
df = pd.read_excel('../data/总表6.23-1.xlsx', sheet_name='区市县派', usecols=[11])
data = df.values
strs = []
for i in range(len(data)):
    strs.append(data[i][0])

# 使用jieba分词
jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
cut_strs = []
for str in strs:
    seg_list = jieba.cut(str,use_paddle=True)  # 使用paddle模式
    cut_strs.append('/'.join(list(seg_list)))


print("cut_strs")