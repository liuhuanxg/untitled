class A():
    def __init__(self):
        self.name = "张三"


class B(A):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def show(self):
        print(self.name)


b = B("李四")
b.show()
