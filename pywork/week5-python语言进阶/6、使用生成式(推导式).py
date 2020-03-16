"""字典推倒式"""

"""
price={
    "AAPL":191.88,
    "GOOG":1186.96,
    "IBM":149.24,
    "ORCL":48.44,
    "ACN":166.89,
    "FB":208.09,
    "SYMC":21.29,
}
#用股票价格大于100元的股票构造一个新字典
# price2={k:price[k] for k in price if price[k]>100}
price2={k:v for k,v in price.items() if v>100}
print(price2)
"""

"""
names=["关羽","张飞","赵云","马超","黄忠"]
courses=["语文","数学","英语"]
#录入五个学生三门课程的成绩
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)
dict1={}
for j in names:
    dict1[j]={}
    for i in courses:
        dict1[j][i]=str(input("请输入{}同学的{}".format(j,i)))
print(dict1)
"""
"""
names=["关羽","张飞","赵云","马超","黄忠"]
courses=["语文","数学","英语"]
dict1={}
for j in names:
    dict1[j]={}
    for i in courses:
        dict1[j][i]=float(input("请输入{}同学的{}成绩：".format(j,i)))
print(dict1)
"""


"""
heapq、itertools等的用法
从列表中找出最大的或最小的N个元素
"""
import heapq

list1=[34,25,12,99,87,63,58,78,88,92]

list2=[
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPL','shares':50,'price':543.22},
    {'name':'FB','shares':200,'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75},
    {'name':'YHOO','shares':45,'price':16.35},
    {'name':'ACME','shares':75,'price':115.65}
]
"""
nlargest(x,list)      在列表中取出最大的x位
nsmallest(x,list)      在列表中取出最小的x位
"""

print(heapq.nlargest(2,list1))
print(heapq.nsmallest(3,list1))
"""

"""
print(heapq.nlargest(2,list2,key=lambda x:x['price']))

# dict1={
#     "关羽":{"语文":100,"数学":89,"英语":90},
#     "张飞":{"语文":79,"数学":89,"英语":80},
#     "赵云":{"语文":70,"数学":80,"英语":93},
#     "马超":{"语文":85,"数学":87,"英语":94},
#     "黄忠":{"语文":91,"数学":80,"英语":94}
# }
list1 = [{"语文": 100, "数学": 89, "英语": 90},
         {"语文": 70, "数学": 80, "英语": 93},
         {"语文": 85, "数学": 87, "英语": 94}]
# list2 = []
list2=[1,3,-4]
list2.sort(key=abs)
print(list2)

# for i in range(1, 101):
#     for b in list1:
#         if b['语文'] <= i and b not in list2:
#             list2.append(b)
#         else:
#             continue
# print(list2)