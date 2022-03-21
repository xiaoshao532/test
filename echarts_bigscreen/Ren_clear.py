import pandas as pd


df = pd.read_csv('../data/rent.csv')
df = df.drop(['mode'], axis=1)
df = df.rename(columns={'community': '楼盘', 'money': '月租/元', 'place': '城区', 'type1': '面积/m²'})
centent1 = []
for i in range(len(df)):
    one = df['面积/m²'][i].replace("\xa0", "").split(' ')
    o = one[0]
    centent1.append(o)
df['居室'] = centent1
centent2 = []
for i in range(len(df)):
    a = df['面积/m²'][i].replace("\xa0", "").split(' ')
    s = a[1]
    centent2.append(s)
df['面积/m²'] = centent2
centent3 = []
for i in range(len(df)):
    a = df['居室'][i].split('室')[0]
    centent3.append(a)

df['居室'] = centent3
centent4 = []
for i in range(len(df)):
    a = df['面积/m²'][i].split('㎡')[0]
    centent4.append(a)
df['面积/m²'] = centent4
df.to_csv('ren_clear1.csv', encoding='utf-8-sig')
