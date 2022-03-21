import pandas as pd

df = pd.read_csv('../data/new.csv')
df = df.rename(columns={'didian': '城区', 'leixing': '类型', 'money': '每平方/元', 'xiaoqu': '小区', 'ziduan1': '销售状态'})
centent1 = []
for i in range(len(df)):
    a = df['城区'][i].split('\xa0')[1]
    centent1.append(a)
# print(centent1)
df['城区'] = centent1
df = df[df['类型'] == "住宅"]
df = df.reset_index(drop=True)
text = df['城区']
text = text.replace('源城区', '源城城区')
text = text.replace('东源县', '东源城区')
text = text.replace('紫金县', '紫金城区')
text = text.replace('和平县', '和平城区')
text = text.replace('龙川县', '龙川城区')
df['城区'] = text
df = df[df['城区'] != '江东新区']
df = df[df['城区'] != '高新区']
df = df[df['城区'] != '连平县']
df = df.reset_index(drop=True)
df.to_csv('../data/new_clear.csv', index=False, encoding='utf_8_sig')
