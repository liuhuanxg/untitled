score=int(input("请输入学习成绩："))
if score>=90 and score<=100:
    print("优秀")
if score>=80 and score<90:
    print("良好")
elif score>=70 and score<80:
    print("一般")
elif score>=60 and score<70:
    print("及格")
else:
    print("不及格")
print('结束')
