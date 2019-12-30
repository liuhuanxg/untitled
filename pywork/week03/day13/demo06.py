# 抛出系统异常
# while True:
#     name=input('请输入姓名：')
#     try:
#         if len(name)<2:
#             raise Exception('错误')
#     except Exception as f:
#         print(f)
#         break

# 抛出自定义异常
# class MyExcept(Exception):
#     def __init__(self,xx):
#         self.xx=xx
#     def __str__(self):
#         return self.xx
# try:
#     raise MyExcept('天上下雨了')
# except MyExcept as f:
#     print(f)

# class ShortExpection(Exception):
#     def __init__(self,length,at_least_len):
#         self.length=length
#         self.at_least_len=at_least_len
#     def __str__(self):
#         return '您输入了{}个字符，最少要{}个字符'.format(self.length,self.at_least_len)
# t=input('请输入字符串：')
# try:
#     raise ShortExpection(len(t),10)
# except ShortExpection as f:
#     print(f)