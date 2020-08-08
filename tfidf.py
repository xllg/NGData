# -*- coding: utf-8 -*-
# @File  : tfidf.py
# @Author: xllg
# @Date  : 2020/8/3 上午9:45
# @Contact : xllgsc@gmail.com

from collections import defaultdict
import math
import operator

"""
函数说明:创建数据样本
Returns:
dataset - 实验样本切分的词条
classVec - 类别标签向量
"""


def loadDataSet():
    dataset = [['来话', '人', '反映', '祥鹤二街', '有', '在', '建', '楼盘', '近期', '通宵', '施工', '噪音', '扰民', '请', '处理'],
                ['来话', '人', '反映', '兴隆街道', '兴隆后街', '竖井', '在', '建', '工地', '每天', '24小时', '施工', '噪音', '分贝',  '过高', '扰民', '严重', '请', '处理'],
                ['来话', '人', '反映', '华阳街道', '麓山大道', '二段', '301号', '的', '成都实验外国语学校',  '（西区/）', '夜间', '施工', '扰民', '噪音', '过大', '请', '处理']]
    return dataset


"""
函数说明：特征选择TF-IDF算法
Parameters:
list_words:词列表
Returns:
dict_feature_select:特征选择词字典
"""
def feature_select(list_words):
    # 总词频统计
    doc_frequency = defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i] += 1

    # 计算每个词的TF值
    word_tf = {}  # 存储每个词的tf值
    for i in doc_frequency:
        word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())

    # 计算每个词的IDF值
    doc_num = len(list_words)
    word_idf = {}  # 存储每个词的idf值
    word_doc = defaultdict(int)  # 存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i] += 1
    for i in doc_frequency:
        word_idf[i] = math.log(doc_num / (word_doc[i] + 1))

    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for i in doc_frequency:
        word_tf_idf[i] = word_tf[i] * word_idf[i]

    # 对字典按值由大到小排序
    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    return dict_feature_select

if __name__ == '__main__':
    data_list = loadDataSet()  # 加载数据
    features = feature_select(data_list)  # 所有词的TF-IDF值
    print(features)
    print(len(features))
