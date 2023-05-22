# 题目十:89、用两种方法去空格
#1
s = "  hello world  "
s = s.replace(" ", "")
print(s)
#2
s = "  hello world  "
l = s.split(" ")
rs = "".join(l)
print(rs)