"""
@File    : 1-时间处理.py
@Time    : 2019/10/17 11:23
"""
import pandas as pd

detail = pd.read_excel('meal_order_detail.xlsx', sheetname=1)
columns = detail.columns
print('列索引columns:\n', columns)

# 1、转换成标准时间格式
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])

# 2、提取时间序列
print(detail['place_order_time'])

"""
年-year  月-month  日-day  小时-hour  分-minute  秒-second
一年中的第几周-week  季节-quarter  weekfyear-一年中的第几周  dayfyear--一年中的第几天
dayfweek- 一周中的第几天  weekday_name-星期名称   is_leap_year-是否是闰年
"""
# 提取日期中的年份
print([i.year for i in detail['place_order_time']])

# 判断处于什么季度
print([i.quarter for i in detail['place_order_time']])

# 判断是否是闰年
print([i.is_leap_year for i in detail['place_order_time']])

# 3、时间运算
"""
年-year  月-month  日-day  小时-hour  分-minute  秒-second
"""
order = pd.read_csv('meal_order_info.csv', encoding='gbk')
columns = order.columns
print('columns:\n', columns)

user_start_time = pd.to_datetime(order['use_start_time'])
lock_time = pd.to_datetime(order['lock_time'])
data_time = lock_time - user_start_time
print(data_time)

# 第二种算法：
# 向后平移一周
use_start_time = pd.to_datetime(order['use_start_time']) + pd.Timedelta(weeks=1)
print(use_start_time)

# 3、分组
detailGroup = detail[['order_id', 'counts', 'amounts']].groupby(by='order_id')
# print(detailGroup.mean())
# print(type(detailGroup.mean()))  # DataFrame
print(detailGroup.mean()['counts'][170])  # 先列再行
print(detailGroup.mean().loc[170, ['counts', 'amounts']])  # loc 先去行再取列
print(detailGroup.mean().iloc[1, :])  # iloc 先切行再切列

# 4、聚合函数
import numpy as np

# 使用agg分别求字段的不同统计函数
print(detail[['counts', 'amounts']].agg([np.sum, np.mean, np.min]))
"""
           counts        amounts
sum   4050.000000  162292.000000
mean     1.110502      44.500137
amin     1.000000       1.000000
"""
# 使用agg分别求字段的不同统计函数

print(detail.agg({'counts': np.sum, 'amounts': [np.mean, np.min]}))
"""
      counts    amounts
amin     NaN   1.000000
mean     NaN  44.500137
sum   4050.0        NaN
"""
# 分组求
print(detailGroup.agg({'counts': np.sum, 'amounts': np.min}))

# 5、聚合函数----transform
print(detail[['counts', 'amounts']].transform(lambda x: x * 2))

"""==============================练习======================================"""
"""求餐馆，每天的营业额"""
import pandas as pd

detail = pd.read_excel('./meal_order_detail.xlsx', sheetname=1)
print(detail)

# 查找出两列
res = detail.loc[:, ['counts', 'amounts']]
detail['sum'] = res['counts'] * res['amounts']

# 获取时间点的日属性，必须是pandas默认支持的时间序列类型
detail.loc[:, 'place_order_time'] = pd.to_datetime(detail.loc[:, 'place_order_time'])

detail.loc[:, 'day'] = [i.day for i in detail.loc[:, 'place_order_time']]

# 以日进行分组，统计pay的sum
res = detail.groupby(by='day')['sum'].sum()
print(res)

# 第二种
# detail['date'] = detail['place_order_time'].dt.date
# detail['amounts'].groupby(detail['date']).sum()

"""求单日菜品销售数目？"""
print(detail[['dishes_name', 'day']].groupby(by='day').count())

"""估计该餐饮店每天的营业时间大概多久？"""
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
max_time = detail[['day', 'place_order_time']].groupby(by='day').max()
min_time = detail[['day', 'place_order_time']].groupby(by='day').min()
time = max_time - min_time
print(time)
