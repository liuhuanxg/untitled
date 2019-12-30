'''
生成随机验证码
'''
import random
def verify_code():
    code=''
    for i in range(4):
        sz=random.randint(0,9)
        xzm=chr(random.randint(97,122))
        dzm=chr(random.randint(65,90))
        c=random.choice([sz,xzm,dzm])
        code=code+str(c)
    return code
print(verify_code())