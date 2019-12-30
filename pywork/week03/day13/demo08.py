'''
工厂模式
'''
# class Bmw():
#     def run(self):
#         print('宝马在跑')
# class Benc():
#     def run(self):
#         print('奔驰在跑')
# class Audi():
#     def run(self):
#         print('奥迪在跑')
# class Factory():
#     @staticmethod
#     def makeCar(name):
#         if name=='宝马':
#             return Bmw()
#         elif name=='奔驰':
#             return Benc()
#         else:
#             return Audi()
# a=Factory.makeCar('宝马')
# b=Factory.makeCar('奔驰')
# c=Factory.makeCar('奥迪')
# a.run()
# b.run()
# c.run()