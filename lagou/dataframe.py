#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dataframe.py
# @Author: YJW
# @Date  : 2018/3/20
# @Desc  :

import pandas as pd
# 数据框操作
import numpy as np
import matplotlib.pyplot as plt
# 绘图
import jieba
# 分词
from wordcloud import WordCloud

# 词云可视化
import matplotlib as mpl
# 配置字体
from pyecharts import Geo

# 地理图
mpl.rcParams[
    "font.sans-serif"
] = [
    "Microsoft YaHei"
]
# 配置绘图风格
plt.rcParams[
    "axes.labelsize"
] =16.

plt.rcParams[
    "xtick.labelsize"
] =14.
plt.rcParams[
    "ytick.labelsize"
] =14.
plt.rcParams[
    "legend.fontsize"
] =12.
plt.rcParams[
    "figure.figsize"
] = [
    15.
    ,
    15.
]
