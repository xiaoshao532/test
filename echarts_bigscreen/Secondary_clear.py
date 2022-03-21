import numpy as np
import pandas as pd
import csv

df = pd.read_excel('../data/secondary.xlsx')
df['a'] = df["l1"].map(str) + df["l2"].map(str) + df["l3"].map(str) + df["l4"].map(str) + df["l5"].map(str) + df[
    "l6"].map(str)
df = df.rename(
    columns={'chaoxiang': '朝向', 'danjia': '每平方（元）', 'diqu': '小区名字', 'diqu2': '城区', 'louceng': '楼层位置', 'square': '面积',
             'time': '建造时间', 'zongjia': '总价', 'a': '格局'})
df = df.drop(['diqu1'], axis=1)
df = df.drop(['diqu3'], axis=1)
df = df.drop(['jianjie'], axis=1)
df = df.drop(['l1'], axis=1)
df = df.drop(['l2'], axis=1)
df = df.drop(['l3'], axis=1)
df = df.drop(['l4'], axis=1)
df = df.drop(['l5'], axis=1)
df = df.drop(['l6'], axis=1)
df[['建造时间']] = df[['建造时间']].astype(str)
centent1 = []
for i in range(len(df)):
    if '年' in df['建造时间'][i]:
        time = df['建造时间'][i].split('年')[0]
        centent1.append(time)
    else:
        time = 0
        centent1.append(time)
# print(centent1)
df['建造时间'] = centent1
df = df[df['建造时间'] != 0]
df = df.reset_index(drop=True)
centent2 = []
for i in range(len(df)):
    if '元' in df['每平方（元）'][i]:
        a = df['每平方（元）'][i].split('元')[0]
        centent2.append(a)
    else:
        a = 0
        centent2.append(a)
# print(centent2)
df['每平方（元）'] = centent2
centent3 = []
for i in range(len(df)):
    if '(' in df['楼层位置'][i]:
        a = df['楼层位置'][i].split('(')[0]
        centent3.append(a)
    else:
        a = 0
        centent3.append(a)
# print(centent3)
df['楼层位置'] = centent3
df = df[df['楼层位置'] != 0]
df = df.reset_index(drop=True)
centent4 = []
for i in range(len(df)):
    if '㎡' in df['面积'][i]:
        a = df['面积'][i].split('㎡')[0]
        centent4.append(a)
    else:
        a = 0
        centent4.append(a)
# print(centent4)
df['面积'] = centent4
df[['每平方（元）']] = df[['每平方（元）']].astype(int)
df[['面积']] = df[['面积']].astype(float)
df[['建造时间']] = df[['建造时间']].astype(int)
df[['总价']] = df[['总价']].astype(float)
df.to_excel('secondary_clear.xlsx', encoding='utf_8_sig', index=False)
