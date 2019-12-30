# class Sheep():
#     def __init__(self):
#         self.cooktime=0
#         self.status='生的'
#     def cook(self,cook_time):
#         self.cooktime=cook_time
#         if self.cooktime<2:
#             self.status='生的'
#         elif self.cooktime>=2 and self.cooktime<4:
#             self.status='半熟'
#         elif self.cooktime>=4 and self.cooktime<6:
#             self.status='熟了'
#         elif self.cooktime>=6:
#             self.status='老了'
#     def __str__(self):
#         return '烤了%d个小时，状态%s'%(self.cooktime,self.status)
# s=Sheep()
# s.cook(5)
# print(s)

class YangRouChuan():
    def __init__(self):
        self.cook_time=0
        self.status='生的'
    def cook(self,cook_time):
        self.cook_time+=cook_time
        if self.cook_time<2:
            self.status='生的'
        elif self.cook_time<4:
            self.status='半熟'
        elif self.cook_time<6:
            self.status='熟了'
        else:
            self.status='老了'
    def __str__(self):
        return '烤了%d个小时，状态%s'%(self.cook_time,self.status)
s=YangRouChuan()
s.cook(2)
print(s)
s.cook(3)
print(s)
s.cook(3)
print(s)