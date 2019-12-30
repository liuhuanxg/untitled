salary=int(input("请输入你的工资："))
if salary>=10000 and salary<20000:
    print('买辆迈腾')
if salary>=20000 and salary<30000:
    print('速腾')
if salary>=30000:
    print('买辆A6')
if salary<=3000:
    print('电动72 35v 50迈，续航：90')


score=int(input("请输入四级成绩："))
if score<60:
    print("下次加油")
else:
    print("恭喜获得四级证书")
print("结束")