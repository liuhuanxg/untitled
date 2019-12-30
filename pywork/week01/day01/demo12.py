a = int(input("请输入："))  # 349
b = 0

b = b * 10 + a % 10
a = a // 10

b = b * 10 + a % 10
a = a // 10

b = b * 10 + a % 10
a = a // 10
print(b)

# 循环
x = int(input("请输入："))
y = 0
while x != 0:
    y = y * 10 + x % 10
    x = x // 10
print(y)