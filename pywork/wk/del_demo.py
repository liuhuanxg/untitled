# class Person():
#     def __init__(self):
#         print('--init--')
#     def __str__(self):
#         return '--str--'
#     def __del__(self):
#         print('--del--')
# def func():
#     per=Person()
#     print(per)
# func()
# print('--finish--')

class Person():
    def __init__(self):
        print('--init--')
    def __str__(self):
        return '--str--'
    def __del__(self):
        print('--del--')
per=Person()
print(per)
print('--finish--')