'''
模块导入的方式：
1.import 模块名
2.import 模块名 as 别名
3.import 模块名1，模块名2，...--一行导入多个模块
'''
import time
print(time.time())

import time as t
print(t.time())

import time,sys,os
print(time.time())
print(sys.path)
print(os.getcwd())