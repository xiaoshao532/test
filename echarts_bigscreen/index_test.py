from sqlalchemy import create_engine
import pandas as pd
# 建立连接引擎
con_engine = create_engine('mysql+pymysql://root:root@localhost:3306/data')
# sql读取所有数据
sql1 = "select * from ren" #score为表名，选择数据库中的数据
sql2 = "select * from sen"
sql3 = "select * from new"
# 将数据赋值给df
df_ren = pd.read_sql_query(sql1, con_engine)
df_sen = pd.read_sql_query(sql2, con_engine)
df_new = pd.read_sql_query(sql3, con_engine)
# print(df)

def get_index_data():
    dict_return = {}
    # c1c2c3环图
    # 出租房
    renNum = df_ren['chengqu'].value_counts()
    ren_type = list(renNum.index)
    ren_counts = renNum.tolist()
    dict_return['ren_type'] = ren_type
    dict_return['ren_counts'] = ren_counts
    dict_return['ren'] = [{"name": item[0], "value": item[1]} for item in list(zip(ren_type, ren_counts))]
    # 二手房
    senNum = df_sen['chengqu'].value_counts()
    sen_type = list(senNum.index)
    sen_counts = senNum.tolist()
    dict_return['sen_type'] = sen_type
    dict_return['sen_counts'] = sen_counts
    dict_return['sen'] = [{"name": item[0], "value": item[1]} for item in list(zip(sen_type, sen_counts))]
    # 新房
    newNum = df_new['chengqu'].value_counts()
    new_type = list(newNum.index)
    new_counts = newNum.tolist()
    dict_return['new_type'] = new_type
    dict_return['new_counts'] = new_counts
    dict_return['new'] = [{"name": item[0], "value": item[1]} for item in list(zip(new_type, new_counts))]

    # r2
    status = df_new['zhuangtai'].value_counts()
    status_type = list(status.index)
    status_counts = status.tolist()
    dict_return['status_type'] = status_type
    dict_return['status_counts'] = status_counts
    dict_return['statu'] = [{"name": item[0], "value": item[1]} for item in list(zip(status_type, status_counts))]

    # l1
    # 二手房
    money_sen_Num = df_sen['money'].groupby(df_sen['chengqu']).mean().reset_index().sort_values('money', ascending=False).reset_index(drop=True)
    sen_zhe_names = money_sen_Num['chengqu'].tolist()
    sen_zhe_counts = money_sen_Num['money'].tolist()
    # 新房
    money_new_Num = df_new['money'].groupby(df_new['chengqu']).mean().reset_index().sort_values('money', ascending=False).reset_index(drop=True)
    new_zhe_names = money_new_Num['chengqu'].tolist()
    new_zhe_counts = money_new_Num['money'].tolist()
    dict_return['sen_zhe_names'] = sen_zhe_names
    dict_return['sen_zhe_counts'] = sen_zhe_counts
    dict_return['new_zhe_names'] = new_zhe_names
    dict_return['new_zhe_counts'] = new_zhe_counts
    print(sen_zhe_names)
    print(new_zhe_names)
    #l2
    # 出租房
    money_Ren_Num = df_ren['money'].groupby(df_ren['chengqu']).mean().reset_index().sort_values('money',ascending=False).reset_index(drop=True)
    new_Ren_names = money_Ren_Num['chengqu'].tolist()
    new_Ren_counts = money_Ren_Num['money'].tolist()
    dict_return['new_Ren_names'] = new_Ren_names
    dict_return['new_Ren_counts'] = new_Ren_counts

    # r1
    xiaoquNum = df_new['money'].groupby(df_new['xiaoqu']).mean().reset_index().sort_values('money', ascending=False).reset_index(drop=True)
    xiaoqu_names = xiaoquNum['xiaoqu'].tolist()
    xiaoqu_counts = xiaoquNum['money'].tolist()
    dict_return['xiaoqu_names'] = xiaoqu_names
    dict_return['xiaoqu_counts'] = xiaoqu_counts

    return dict_return
print(get_index_data())