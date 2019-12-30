"""
该代码，进行成绩等级判断
分为优秀、良好、一般、及格和不及格
"""
score=80
if score>=90:     #成绩90以上，输出优秀
    print("优秀")
elif score>=80:
    print("良好")
elif score>=70:
    print("一般")
elif score>=60:
    print("及格")
else:
    print("不及格")