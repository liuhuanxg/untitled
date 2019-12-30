class A():
    books=['三国','西游记']
    def __init__(self,name):
        self.name=name
x=A('张三')
y=A('李四')
x.books[0]='水浒传'
print(x.books)
print(y.books)
print(A.books)

x.books=['红楼梦','大秦帝国']
print(x.books)
print(y.books)
print(A.books)