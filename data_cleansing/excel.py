import pandas as pd
import numpy as np
import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='end_project', port=3306, charset='utf8')
cursor = conn.cursor()


# 数据1
# df = pd.read_excel(r'F:\real_python\git_project\data_cleansing\数据1.xlsx')
# datas = np.array(df).tolist()
# print(type(datas))
# for data in datas:
#     print(data)
#     for i in range(len(data)):
#         if not isinstance(data[i], str):
#             data[i] = str(data[i])
#     sql = "insert into t_excel (name,academic,job_exp,exper,age,census,job_addr,job_salary,job_ind,job_status,addr,birthday,email,phone) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
#     cursor.execute(sql, [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13]])
#     conn.commit()
# 数据2
# df = pd.read_excel(r'F:\real_python\git_project\data_cleansing\数据2.xlsx')
# datas = np.array(df).tolist()
# print(type(datas))
# for data in datas:
#     print(data)
#     for i in range(len(data)):
#         if not isinstance(data[i], str):
#             data[i] = str(data[i])
#     sql = "insert into t_excel (name,marry,academic,job_exp,exper,age,census,job_addr,job_salary,job_ind,job_status,addr,birthday,email,phone) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)"
#     cursor.execute(sql, [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14]])
#     conn.commit()

# 数据3

df = pd.read_excel(r'F:\real_python\git_project\data_cleansing\数据3.xlsx')
datas = np.array(df).tolist()
print(type(datas))
for data in datas:
    print(data)
    for i in range(len(data)):
        if not isinstance(data[i], str):
            data[i] = str(data[i])
    sql = "insert into t_excel (name,marry,academic,job_exp,exper,age,census,job_addr,job_p,job_salary,job_ind,job_status,addr,birthday,email,phone) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)"
    cursor.execute(sql, [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15]])
    conn.commit()