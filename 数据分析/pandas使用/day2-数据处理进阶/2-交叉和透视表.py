"""
@File    : 2-交叉和透视表.py
@Time    : 2019/10/17 16:57
"""
import numpy as np
import pandas as pd

# 透视表  index--行分组键
"""
透视表是一种plus版的分组聚合
data  DataFrame数据
values 最终统计指标的所针对对象，要关心的数据主体
index 按照行进行分组
columns  按照columns进行列分组
aggfunc   对主体进行什么指标的统计
"""
detail = pd.read_excel('./meal_order_detail.xlsx', sheetname=1)
detail_pivot = pd.pivot_table(data=detail[['order_id', 'counts', 'amounts']], index='order_id',
                              aggfunc=np.sum)
detail_pivot1 = pd.pivot_table(data=detail[['order_id', 'counts', 'amounts', 'dishes_name']],
                               index=['order_id', 'dishes_name'],
                               aggfunc=np.sum)
# print(detail_pivot1)

detail_pivot2 = pd.pivot_table(data=detail[['order_id', 'counts', 'amounts', 'dishes_name']].head(),
                               index='order_id',
                               columns='dishes_name',
                               aggfunc=np.sum)
# print(detail_pivot2)

data = pd.DataFrame({'name': ['a', 'b', 'c', 'd'], 'class': ['1', '1', '2', '2'], 'age': [5, 7, 8, 10],
                     'sex': ['男', '男', '男', '女', ]})
res = pd.pivot_table(data=data, index='name', columns='class')
res1 = pd.pivot_table(data=data, index='name', columns='class', values='age')
# print(res)
# print(res1.index)

# fill_values 默认空值的显示
res2 = pd.pivot_table(data=data, index='name', columns='class', values='age', fill_value='无')
print(res2)
"""
class  1  2   3
name           
a      5  无   无
b      7  无   无
c      无  8   无
d      无  无  10
"""
# dropna--是否删除全为Nan的列 参数：True为删除   注意：dropna与fill_values不能同时使用
res3 = pd.pivot_table(data=data, index='name', columns='class',
                      fill_value='无')

print(res3)
res4 = pd.pivot_table(data=data, index='name', columns='class',
                      dropna=True, margins=True)
print(res4)


"""========================交叉表================================"""
print(pd.crosstab(index=detail['order_id'], columns=detail['dishes_name'], values=detail['counts']))