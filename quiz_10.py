# -*- coding: utf-8 -*-
# 题目十:108、python中读取Excel文件的方法
import pandas as pd
#f = open('example.xlsx')
#data = f.read()
#print(data)
#f.close()
df = pd.read_excel('example.xlsx')
print(df)