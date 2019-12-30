a={'001':{'name':'张三','age':18},
   '002':{'name':'李四','age':28},
   '003':{'name':'王五','age':19},
   '004':{'name':'赵六','age':31},
}

def find(num):
    for k in a.keys():
        if k==num:
            return True
    else:
        return False

def add():
    print('请输入您想要添加的学生信息：')
    num=input('编号：')
    for i in a.keys():
        if num==i:
            print('编号重复，添加失败')
            break
    else:
        name=input('姓名：')
        age=input('年龄：')
        a[num]={'name':name,'age':int(age)}

def delete(num):
    if find(num):
        del a[num]
    else:
        print('没有该学生')

def update(num):
    if find(num):
        name = input('姓名：')
        age = input('年龄：')
        a[num] = {'name': name, 'age': int(age)}
    else:
        print('没有该学生')

def findAll():
    for i in a.items():
        print(i)

while True:
    print('1.增')
    print('2.删')
    print('3.改')
    print('4.查某个')
    print('5.查全部')
    print('0.退出')
    choice=int(input('请输入选择：'))
    if choice==1:
        add()
    elif choice==2:
        num = input('请输入想要删除的编号')
        delete(num)
    elif choice==3:
        num = input('请输入想要更新的编号')
        update(num)
    elif choice==4:
        num=input('请输入想要查询的编号')
        if find(num):
            print(num,':',a[num])
        else:
            print('没有该学生')
    elif choice==5:
        findAll()
    elif choice==0:
        break