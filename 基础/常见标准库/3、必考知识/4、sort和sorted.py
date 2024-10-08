# sort是在原基础上进行改动,直接对原列表进行操作
# 是sorted不在原列表基础上改动，需要进行赋值操作，赋给新的列表

c1 = [10, 5, 2, 9, 4, 2]
c4 = c1.sort()
print(c1)  # [2, 2, 4, 5, 9, 10]
print(c4)  # None

c2 = [2, 1, 5, 3, 6, 8]
c3 = sorted(c2)
print(c3)  # [1, 2, 3, 5, 6, 8]
print(c2)  # [2, 1, 5, 3, 6, 8]
