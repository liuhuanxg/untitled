import  time
class  Oper():
    @staticmethod
    def getUserList():
       userList=[]
       with open('user.txt','r')as f :
           line=f.readline()
           while len(line)>0:
               con=line[0:-1]
               print(con)
               userList.append(eval(con))
               line=f.readline()
       return  userList
    @staticmethod
    def register():
        userList=Oper.getUserList()
        while True:
            username=input('请输入用户名：')
            password=input('请输入密码：')
            for one in userList:
                    if one[0]==username:
                        print('账户名重复。')
                        break
            else:
                if len(password)<=2 or password[-2]!='@':
                    print('密码格式有误。')
                    break
                for xhx in password:
                    if xhx=='_':
                        print('账号注册成功。')
                        break
                else:
                        print('没有下划线，请重新输入。')
                        continue
                lb = []
                lb.append(username)
                lb.append(password)
                lb.append(0)
                with open('user.txt', 'a') as f:
                    f.write(str(lb))
                    f.write('\n')
            break
    @staticmethod
    def login():
         userList=Oper.getUserList()
         i=1
         while i<=3:
             username=input('请输入用户名：')
             password=input('请输入密码：')
             for one in userList:
                 if one[0]==username and one[1]==password:
                     print('登录成功')
                     return username
             else:
                 if i !=3:
                     print('用户名密码错误三次您还有%d次机会'%(3-i))
                 else:
                     print('三次错误没机会了')
             i+=1
         return None
    @staticmethod
    def cunqian(dluser):
        userList=Oper.getUserList()
        money=float(input('请输入存钱数：'))
        with open('user.txt','w')as f:
            for one in userList:
                if dluser==one[0]:
                    one[2]+=money
                f.write(str(one))
                f.write('\n')
        with open('b.txt','a')as f:
            strTime=time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime())
            f.write(dluser)
            f.write(':')
            f.write(strTime)
            f.write(',+')
            f.write(str(money))
            f.write('\n')
    @staticmethod
    def quqian(dluser):
        userList = Oper.getUserList()
        money = float(input('请输入取钱数：'))
        with open('user.txt', 'w')as f:
            for one in userList:
                if dluser == one[0]:
                    if money<=one[2]:
                        one[2] -= money
                        with open('b.txt', 'a')as f:
                            strTime = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime())
                            f.write(dluser)
                            f.write(':')
                            f.write(strTime)
                            f.write(',-')
                            f.write(str(money))
                            f.write('\n')
                    else:
                        print('账户余额不足。')
                f.write(str(one))
                f.write('\n')
                break

    @staticmethod
    def jyrs():
        a=set()
        with open('b.txt','r')as f :
            line=f.readline()
            while len(line)>0:
                lb=line.split(':')
                a.add(lb[0])
                line=f.readline()
            for x in a:
                print(x)
dluser=None
while True:
    bh=int(input('请输入编号：'))
    if bh==1:
        Oper.register()
    elif bh==2:
        dluser=Oper.login()
    elif bh==3:
        if dluser!=None:
            Oper.cunqian(dluser)
        else:
            print('请先登录。')
    elif bh==4:
        if dluser!=None:
            Oper.quqian(dluser)
        else:
            print('请先登录。')
    elif bh==5:
        Oper.jyrs()
    elif bh==0:
        exit(0)
    else:
        print('编号输入有误，请重新输入。')
