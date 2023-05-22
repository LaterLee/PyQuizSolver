# 题目十:108、python中读取Excel文件的方法
import pandas as pd
f = open(r'C:\Users\Asus\Desktop\example.xlsx','r')
data = f.read()
df = pd.read_excel()
print(data)
f.close()