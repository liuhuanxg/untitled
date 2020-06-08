#-*-coding:utf-8 -*-
print(111)
"""
列表增加操作主要有：
    append(object)：         在列表末尾添加数据
    insert(index,object)     在列表某个位置插入数据，超出列表长度不报错    
    extend(iterable)         添加一个可迭代对象
Version: 0.1
Author: youzi
"""
names = ["柚子", "西瓜"]
names.append("榴莲")
print(names)    #['柚子', '西瓜', '榴莲']

names.insert(10, "桃子")
print(names)    #['柚子', '西瓜', '榴莲', '桃子']
names.extend("苹果")
print(names)    #['柚子', '西瓜', '榴莲', '桃子', '苹', '果']

names[0] = "哈密瓜"
print(names)    #['哈密瓜', '西瓜', '榴莲', '桃子', '苹', '果']

for name in names:
    print(name)

print(names.index("西瓜"))
print(names.count("西瓜"))

names.remove("西瓜")
print(names)
names.pop(0)
print(names)

del names[0]
print(names)
names.clear()
print(names)

"""
用户信息录入系统
    开发步骤
    1、定义一个首页界面[告诉我们要做什么] 
    2、通过列表保存数据
    3、通过用户输入的选项，执行判断
    4、实现各项的功能
    5、测试功能运行是否正确
    6、BUG 完善
"""

# 保存所有伙伴的列表
sheng_lou = list()
while True: # 首页
    print("欢迎来到蜃楼用户管理系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print(" 1、查看所有小伙伴")
    print(" 2、录入个人信息")
    print(" 3、查看个人信息")
    print(" 4、退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~") # 用户输入选项
    c = input("请输入您的选项:")
    if c == "1":  # 遍历所有小伙伴
        for stu in sheng_lou:
            print("小伙伴：", stu)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("查看完成按任意键返回首页.")
    elif c == "2":  # 提示用户输入姓名
        name = input("请输入昵称：")
        if name in sheng_lou:
            input("该昵称已经存在，请使用其他昵称录入")
            continue
        # 保存昵称:列表的末尾追加
        sheng_lou.append(name)
        input("录入完成，按任意键返回首页...")
    elif c == "3":  # 提示用户输入要查看的昵称
        nickname = input("请输入要查看的昵称：")  # 成员成员运算符，判断昵称是否包含在列表中[True/False]
        if nickname in sheng_lou:
            print("该成员已经在大厅中.")
        else:
            print("该昵称代表的成员没有在大厅中.")
            input("查看个人信息，正在升级中...")
    elif c == "4":
        input("退出系统，保存好个人数据，按任意键退出")
        exit(1)