from  admin import   Admin
import  time
from  atm import  ATM


def main():
    # 管理员对象
    admin = Admin()
    #管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return  -1

    allUsers={}

    atm=ATM()

    while True:
        admin.printsysFunctionView()
        #等待用户的操作
        option=input("请输入您的操作：")
        if option=="1":
            atm.creatUser()
        elif option == "2":
            atm.serachUserInfo()
        elif option == "3":
            print('取款')
        elif option == "4":
            print('存储')
        elif option == "5":
            print('转账')
        elif option == "6":
            print('改密')
        elif option == "7":
            print('锁定')
        elif option == "8":
            print('解锁')
        elif option == "9":
            print('补卡')
        elif option == "0":
            print('销户')
        elif option == "t":
            if not admin.adminOption():
                return  -1
                print("退出成功")
        time.sleep(1)

if __name__=="__main__":
    main()