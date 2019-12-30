'''
包的导入
'''
# import sys
# print(sys.path)
# sys.path.append('E:\\pywork\\day08\\p1')
# import demox
# print(demox.qh(2,3))

# import day08.p1.demox
# print(day08.p1.demox.qh(3,4))

# from day08.p1.demox import qh
# print(qh(3,4))

# 报错
# from day08.p1 import demox.qh
# print(demox(3,4))

# from day08.p1 import demox
# print(demox.qh(3,4))

# from day08.p1.demox import qh
# from day08.p1.demox2 import qj,qd
# print(qh(2,3))
# print(qj(2,3))
# print(qd(2,3))

# from day08.p1 import demox2,demox
# print(demox.qh(1,2))
# print(demox2.qj(2,3))

'''
*导入时，__init__中的方法可执行，demox中的不行
'''
# from day08.p1 import *
# # demox.qh(2,3)     # 报错
# prt()

'''
*导入时，__init__中的方法可执行，demox中的不行
在__init__.py中使用__all__列表存放(demox模块名和prt方法名)，里面的就可以被执行了
'''
from week02.day08.p1 import *
print(demox.qh(2, 3))
prt()