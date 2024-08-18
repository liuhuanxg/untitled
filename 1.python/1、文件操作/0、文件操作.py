#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 0、文件操作.py
@Time: 2020/5/24 23:21
@user：liuhuan   
"""
"""
r  只读     r+ 可读可写
w  覆盖写   w+ 可读可覆盖写
r  追加写   r+ 可读可追加写

'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
"""


with open("test.txt","r") as fp:
    result = fp.read()
    print(result)

with open("test.txt","a+") as fp:
    fp.write("hello java")
    result = fp.read()
    print(result)