#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 4、字典.py
@Time: 2020/6/6 22:13
@user：liuhuan   
"""

# 查看数据
dct={'username': 'waltz', 'nickname': '柚子'}
print(dct.items())  # dict_items([('username', 'waltz'), ('nickname', '柚子')])
print(dct.keys())  # dict_keys(['username', 'nickname'])
print(dct.values()) #dict_values(['waltz', '柚子'])
print(dct.get("nickname")) #'柚子'
print(dct.get("age"))   # None
print(dct.get("age","西瓜")) # 西瓜
print(dct["nickname"])#'柚子'

# 修改数据
dct["nickname"] = "桃子"
dct.update({"username":"youzi"})
print(dct)
dct.setdefault("username", "xigua")
dct.setdefault("age", 24)
print(dct)

# 删除数据
dct={'username': 'waltz', 'nickname': '柚子', "age":24}
value = dct.pop("username")
print(value)  # waltz
print(dct)
result = dct.popitem()
print(result)  #('age', 24)

r = dct.clear()
print(r)
print(dct)

dct={'username': 'waltz', 'nickname': '柚子', "age":24}
for key in dct:
    print(key,dct[key])

for value in dct.values():
    print(value)

for key,value in dct.items():
    print(key,value)