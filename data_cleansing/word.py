import os,time
from win32com import client

for i in os.listdir(r'F:\real_python\git_project\data_cleansing\word'):
    print(i)
    path=r'F:\real_python\git_project\data_cleansing\word'+'\\'+i
    print(path)
    word = client.Dispatch('Word.Application')
    try:
        doc = word.Documents.Open(path)  # 目标路径下的文件
        list1 = i.split('.')
        doc.SaveAs(r'F:\real_python\git_project\data_cleansing\txt'+'\\'+list1[0]+'.txt', 4)  # 转化后路径下的文件
        doc.Close()
        word.Quit()
    except:
        print('加入失败', i)
# # time.sleep(3)
import os
# from win32com import client
#
# path = r'F:\real_python\git_project\data_cleansing\word\吉克阿铁_18712852106.doc'
# word = client.Dispatch('Word.Application')
# doc = word.Documents.Open(path)  # 目标路径下的文件
# doc.SaveAs(r'F:\real_python\git_project\data_cleansing\txt\吉克阿铁_18712852106.txt', 4)  # 转化后路径下的文件
# doc.Close()
# word.Quit()