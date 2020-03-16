class Father:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        print(self.__age)


class Son(Father):
    def __init__(self,name,age):
        super().__init__(name,age)
        # self.name = name
        pass

    def get_name(self):
        print(self.name)
        # print(self.age)


s = Son("11",22)
s.get_name()
s = open('demo.py',"r",newline='')
r = s.read()
print(r)

import csv
writer = csv.writer()

