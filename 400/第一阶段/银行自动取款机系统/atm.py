from  user import User
from  card import  Card
import  random

class ATM(object):
    def __init__(self):
        self.allUsers={}


    #开户
    def creatUser(self):
        name=input("请输入姓名：")
        idCard=input('请输入您的身份证号码：')
        phone=input('请输入您的电话号码：')
        prestoreMoney=int(input('请输入预存金额：'))
        if prestoreMoney< 0:
            print("预存有误")
            return -1
        onePasswd=input('请设置密码：')
        #验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！！开户失败……")
            return -1
        #生成卡号
        cardStr=self.randomCardId()

        #将用户信息储存进allUsers
        card=Card(cardStr, onePasswd, prestoreMoney)
        user=User(name,idCard,phone,card)
        self.allUsers[cardStr]=user
        print('开户成功！！，请记好卡号(%s)……'%(cardStr))
        print(self.allUsers)

    #查询
    def serachUserInfo(self):
        cardNum=input('请输入您的卡号：')
        #验证卡号是否存在
        user=self.allUsers.get(cardNum)
        if not user:
            print('卡号不存在！！查询失败……')
            return  -1
        if not self.checkPasswd(user.card.cardPasswd):
              print('密码输入错误，查询失败……')
              return  -1
        print('账号：%s   余额：%d'%(user.card.cardId,user.card.cardMoney))
    #取款
    def getMoney(self):
        pass
    # 存钱
    def saveMoney(self):
        pass
    #转账
    def transferMoney(self):
        pass
    #改密
    def changePasswd(self):
        pass
    #锁定
    def lockUser(self):
        pass
    #解锁
    def unlockUser(self):
        pass
    # 补卡
    def newCard(self):
        pass
    # 销户
    def killUsers(self):
        pass

    #验证密码
    def checkPasswd(self,realPasswd):

        for i in range(3):
              tempPasswd = input('请输入密码：')
              if tempPasswd==realPasswd:
                  return  True
        return False
    #生成卡号
    def randomCardId(self):
        while True:
             str=''
             for i in range(6):
                ch =chr(random.randrange(ord('0'),ord('9')+1))
                str+=ch
             return str
             #判断卡号是否重复
             if not self.allUsers.get(str):
                 return  str
