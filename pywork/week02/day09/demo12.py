class House():
    def __init__(self,info,area,address):
        self.info=info
        self.area=area
        self.address=address
        self.furnitures=[]
    def addFurniture(self,obj):
        self.area-=obj.area
        self.furnitures.append(obj.name)
    def __str__(self):
        s1='户型{}，面积{}，地址{}，'.format(self.info,self.area,self.address)
        s2='室内家具有：'
        for f in self.furnitures:
            s2+=f+' '
        return s1+s2
class Furniture():
    def __init__(self,name,area):
        self.name=name
        self.area=area
h1=House('三室一厅',138,'北京大兴')
bed=Furniture('床',6)
h1.addFurniture(bed)
print(h1)
table=Furniture('桌子',3)
h1.addFurniture(table)
print(h1)
sofa=Furniture('沙发',10)
h1.addFurniture(sofa)
print(h1)