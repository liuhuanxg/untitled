'''
1-2+3-4...+99
方法1
'''
# i = 1
# zf = -1
# sum = 0
# while abs(i) < 100:
#     sum += i
#     i = abs(i) + 1
#     i = i * zf
#     zf *= -1
# print(sum)

'''
1-2+3-4...+99
方法2
'''
# i=1
# sum=0
# while i<100:
#     sum+=(-1)**(i-1)*i
#     i+=1
# print(sum)

'''
1-2+3-4...+99
方法3
'''
# n = 1
# sum = 0
# while n < 100:
#     if n % 2 == 0:
#         sum -= n
#     else:
#         sum += n
#     n += 1
# print(sum)