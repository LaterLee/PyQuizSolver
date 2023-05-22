# 题目三:69、请将[i for i in range(3)]改成生成器
#原格式
a = [i for i in range(3)]
t_1 = type(a)
#修改后
a_r = (i for i in range(3))
t_2 = type(a_r)
print("修改前格式:",t_1)
print("修改后格式:",t_2)