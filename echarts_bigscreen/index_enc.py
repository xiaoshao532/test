import pandas as pd
df_ren = pd.read_excel('../data/ren_clear2.xlsx')
df_sen = pd.read_excel('../data/secondary_clear.xlsx')
df_new = pd.read_csv('../data/new_clear.csv')

def get_index_data():
    dict_return = {}
    # c1c2c3环图
    # 出租房
    renNum = df_ren['城区'].value_counts()
    ren_type = list(renNum.index)
    ren_counts = renNum.tolist()
    dict_return['ren_type'] = ren_type
    dict_return['ren_counts'] = ren_counts
    dict_return['ren'] = [{"name": item[0], "value": item[1]} for item in list(zip(ren_type, ren_counts))]
    # 二手房
    senNum = df_sen['城区'].value_counts()
    sen_type = list(senNum.index)
    sen_counts = senNum.tolist()
    dict_return['sen_type'] = sen_type
    dict_return['sen_counts'] = sen_counts
    dict_return['sen'] = [{"name": item[0], "value": item[1]} for item in list(zip(sen_type, sen_counts))]
    # 新房
    newNum = df_new['城区'].value_counts()
    new_type = list(newNum.index)
    new_counts = newNum.tolist()
    dict_return['new_type'] = new_type
    dict_return['new_counts'] = new_counts
    dict_return['new'] = [{"name": item[0], "value": item[1]} for item in list(zip(new_type, new_counts))]

    # r2
    status = df_new['销售状态'].value_counts()
    status_type = list(status.index)
    status_counts = status.tolist()
    dict_return['status_type'] = status_type
    dict_return['status_counts'] = status_counts
    dict_return['statu'] = [{"name": item[0], "value": item[1]} for item in list(zip(status_type, status_counts))]

    # l1
    # 二手房
    money_sen_Num = df_sen['每平方（元）'].groupby(df_sen['城区']).mean().reset_index().sort_values('每平方（元）', ascending=False).reset_index(drop=True)
    sen_zhe_names = money_sen_Num['城区'].tolist()
    sen_zhe_counts = money_sen_Num['每平方（元）'].tolist()
    # 新房
    money_new_Num = df_new['每平方/元'].groupby(df_new['城区']).mean().reset_index().sort_values('每平方/元', ascending=False).reset_index(drop=True)
    new_zhe_names = money_new_Num['城区'].tolist()
    new_zhe_counts = money_new_Num['每平方/元'].tolist()
    dict_return['sen_zhe_names'] = sen_zhe_names
    dict_return['sen_zhe_counts'] = sen_zhe_counts
    dict_return['new_zhe_names'] = new_zhe_names
    dict_return['new_zhe_counts'] = new_zhe_counts
    print(sen_zhe_names)
    print(new_zhe_names)
    #l2
    # 出租房
    money_Ren_Num = df_ren['月租/元'].groupby(df_ren['城区']).mean().reset_index().sort_values('月租/元',ascending=False).reset_index(drop=True)
    new_Ren_names = money_Ren_Num['城区'].tolist()
    new_Ren_counts = money_Ren_Num['月租/元'].tolist()
    dict_return['new_Ren_names'] = new_Ren_names
    dict_return['new_Ren_counts'] = new_Ren_counts

    # r1
    xiaoquNum = df_new['每平方/元'].groupby(df_new['小区']).mean().reset_index().sort_values('每平方/元', ascending=False).reset_index(drop=True)
    xiaoqu_names = xiaoquNum['小区'].tolist()
    xiaoqu_counts = xiaoquNum['每平方/元'].tolist()
    dict_return['xiaoqu_names'] = xiaoqu_names
    dict_return['xiaoqu_counts'] = xiaoqu_counts

    return dict_return
print(get_index_data())