'''
策略模式
'''
# class CashNorm():
#     def accept_money(self,money):
#         return money
# class Cash_rate():    # 打折
#     def __init__(self,rate):
#         self.rate=rate
#     def accept_money(self,money):
#         return self.rate*money
# class Cash_condition():    # 满减
#     def __init__(self,condition,ret):
#         self.condition=condition
#         self.ret=ret
#     def accept_money(self,money):
#         if money<self.condition:
#             return money
#         else:
#             return money-money//self.condition*self.ret
# class Context():
#     def __init__(self,style):
#         self.style=style
#     def getResult(self,money):
#         return self.style.accept_money(money)
# if __name__=='__main__':
#     a={}
#     a[0]=Context(CashNorm())
#     a[1]=Context(Cash_rate(0.8))
#     a[2]=Context(Cash_condition(300,50))
#     style=int(input('请输入优惠方式：'))
#     if style>2:
#         style=0
#     money=float(input('请输入金额：'))
#     print(a[style].getResult(money))