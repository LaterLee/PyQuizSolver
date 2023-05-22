# 题目六:84、递归求和
def get_sum_recursive(num):
    if num >= 1:
        s = num + get_sum_recursive(num-1)
    else:
        s = 0
    return s

s = get_sum_recursive(10)
print("10递归求和为；",s)  