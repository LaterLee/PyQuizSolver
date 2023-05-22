# 题目二:14、python中生成随机整数、随机小数、0--1之间小数方法
import random
import numpy as np
rz = random.randint(1, 10)
print("随机整数为:",rz)
rq = np.random.randn(5)
print("5个随机小数为:",rq)
r = random.random()
print("0—1随即小数为:",r)