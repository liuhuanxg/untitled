import pandas as pd
import numpy as np

details=pd.read_excel('meal_order_detail.xlsx')

pivot=pd.pivot_table(details[['order_id','counts','amounts']],index='order_id')
print('透视表前五条数据：',pivot.head())

pivot=pd.pivot_table(details[['order_id','counts','amounts']],index='order_id',aggfunc=np.sum)
print('透视表前五条(求和--聚合)数据：\n',pivot.head())


#以order_id(行)和dishes_name（列）作为分组创建的透视表：
pivot=pd.pivot_table(details[['order_id','dishes_name','counts','amounts']],index='order_id',columns='dishes_name',aggfunc=np.sum)
print('以order_id和dishes_name作为分组条件创建的透视表：',pivot.head())

