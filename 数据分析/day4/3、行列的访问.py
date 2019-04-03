import pandas as pd

details=pd.read_excel('meal_order_detail.xlsx')


#获取某一列数据
dishes_name=details['dishes_name']
# print(dishes_name)

#获取多行数据，
detail_pre6=details[:2]
print(detail_pre6)

#整个表前五行数据
print('前五行数据：',details.head())
print('后五行数据：',details.tail())

#loc切片方法
detail_r6=details.loc[1:7,['dishes_name','amounts']]
print(detail_r6)
s=details.keys()
print(s)
print('---------------------------------')
# for i in details.items():
#     print(i[1][0])
    # print(type(i))


#筛选出order_id=458，dishes_name和amounts的数据
result=details.loc[details['order_id']==458,['dishes_name','amounts']]
print('order_id=458的数据：',result)