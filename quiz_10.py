# 题目十:108、python中读取Excel文件的方法
import pandas as pd
f = open('example.xlsx')
data = f.read()
df = pd.read_excel()
print(data)
f.close()