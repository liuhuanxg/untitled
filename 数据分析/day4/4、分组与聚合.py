import pandas as pd

details=pd.read_excel('meal_order_detail.xlsx')

#分组
detailGroup=details[['order_id','counts','amounts']].groupby(by='order_id')
# print(type(detailGroup))
# for i in detailGroup:
#     print(i)
print('分组后的前5组数据的平均数：',detailGroup.mean().head())
print('标准差：',detailGroup.std().head())
print('每组的数据个数:',detailGroup.size().head())