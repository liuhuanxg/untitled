class A():
    def __init__(self):
        self.tax=0.1
x=A()
print(x.tax)
delattr(x,'tax')
print(x.tax)    # 'A' object has no attribute 'tax'