# 题目九:102、生成0-100的随机数
import random
rn1 = random.randint(0, 100)
rn2 = 100*random.random()
rn3 = random.choice(range(0,101))
print("rn1=",rn1)
print("rn2=",rn2)
print("rn3=",rn3)