# -*- coding: utf-8 -*-
# @File  : jieba_03_extract_tags.py
# @Author: xllg
# @Date  : 2020/7/23 上午10:26
# @Contact : xllgsc@gmail.com

import jieba.analyse

text = '关键词是能够表达文档中心内容的词语，常用于计算机系统标引论文内容特征、' \
       '信息检索、系统汇集以供读者检阅。关键词提取是文本挖掘领域的一个分支，是文本检索、' \
       '文档比较、摘要生成、文档分类和聚类等文本挖掘研究的基础性工作'

keywords = jieba.analyse.extract_tags(text, topK=20, withWeight=True, allowPOS=())
print(keywords)
