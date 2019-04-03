import hashlib
s='1111'
m=hashlib.md5()
m.update(s.encode('utf-8'))
pwd=m.hexdigest()
print(pwd)

m.update(pwd.encode('utf-8'))
new_pwd=m.hexdigest()
print(new_pwd)

m=hashlib.md5()
m.update(pwd.encode('utf-8'))
s_pwd=m.hexdigest()
print(s_pwd)