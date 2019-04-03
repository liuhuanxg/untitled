import requests
import hashlib
import re

sess = requests.session()


def lagou_login(name, pwd):
    login_header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'passport.lagou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    }
    # 获取登录页
    r = sess.get('https://passport.lagou.com/login/login.html', headers=login_header)

    # 正则匹配 token 和 code
    pattern = re.compile(r".*window.X_Anti_Forge_Token = '(.*?)'.*")
    token = pattern.findall(r.text)[0]

    pattern1 = re.compile(r".*window.X_Anti_Forge_Code = '(.*?)'.*")
    code = pattern1.findall(r.text)[0]
    # 计算密码

    md = hashlib.md5()
    md.update(pwd.encode('utf-8'))
    password = md.hexdigest()

    md = hashlib.md5()  # 还是需要实例化 md5
    md.update('veenike'.encode() + password.encode('utf-8') + 'veenike'.encode())
    password = md.hexdigest()
    print(password)
    # exit()
    data = {
        'isValidate': 'true',
        'username': name,
        'password': password,
        'request_form_verifyCode': '',
        'submit': '',
        # 'challenge': 'f87c0e9f9dfbd5aaedadd842b7a6a373',
    }

    heade = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': str(len(data)),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'passport.lagou.com',
        'Origin': 'https://passport.lagou.com',
        'Referer': 'https://passport.lagou.com/login/login.html?ts=1540352509382&serviceId=account&service=https%253A%252F%252Faccount.lagou.com%252Fv2%252Faccount%252Fuserinfo.html&action=login&signature=C787A04AD3F7846C9CE41ED83F6716CC',
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/69.0.3497.81Safari/537.36',
        'X-Anit-Forge-Code': code,
        'X-Anit-Forge-Token': token,
        'X-Requested-With': 'XMLHttpRequest',
    }

    url = 'https://passport.lagou.com/login/login.json'  # 登录地址
    pro = {'http': '106.75.226.36:808'}  # 代理
    r = sess.post(url, data=data, proxies=pro, headers=heade)  # 发起登录请求
    json_data = r.json()
    print(json_data['message'])


if __name__ == '__main__':
    uname = input('请输入用户名：')
    pwd = input('请输入密码:')
    lagou_login(uname, pwd)
