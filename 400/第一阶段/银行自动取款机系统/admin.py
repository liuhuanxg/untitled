import time
class Admin(object):
    admin="1"
    passwd="1"
    def printAdminView(self):
        print("**************************************************************")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                    欢迎登陆西瓜银行                        *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("**************************************************************")
    def adminOption(self):
        inputadmin=input("请输入管理员账号：")
        if self.admin!=inputadmin:
            print("账号输入有误！")
            return  -1
        inputpasswd=input("请输入管理员密码：")
        if self.passwd!=inputpasswd:
            print("密码输入有误！")
            return -1
        print("操作成功！请稍候……")
        time.sleep(2)
        return  0
    def printsysFunctionView(self):
        print("**************************************************************")
        print("*                                                            *")
        print("*                        西瓜银行                            *")
        print("*          开户(1)                         查询(2)           *")
        print("*          取款(3)                         存款(4)           *")
        print("*          转账(5)                         改密(6)           *")
        print("*          锁定(7)                         解锁(8)           *")
        print("*          补卡(9)                         销户(0)           *")
        print("*                         退出(t)                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("**************************************************************")

