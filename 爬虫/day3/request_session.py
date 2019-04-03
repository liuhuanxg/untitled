import requests
from http import cookiejar

cookie = cookiejar.MozillaCookieJar()
sess = requests.session()
url = 'http://www.renren.com/PLogin.do'
header = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
}
data = {
    'email': '18519020313',  # 用户名
    'password': 'hua7700969'  # 密码
}
response = sess.post(url=url, data=data, headers=header)
# cookie.load('cookie.txt')
# print(cookie)
# print(response.cookies)
# # print(response.text)
# # r = sess.get('http://www.renren.com/310303067/profile')
# #
# print(requests.utils.dict_from_cookiejar(cookie))
# # print(r.text)


# Request URL: https://passport.lagou.com/login/login.json

'''

isValidate: true
username: 18611641684
password: f79d98f4e23de3cce9dec8557aa0ceba
request_form_verifyCode: 
submit: 
challenge: 4e98b2f6516a7f953209e61b254c909f

'''
