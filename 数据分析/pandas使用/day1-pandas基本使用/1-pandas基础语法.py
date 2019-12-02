import pandas as pd

"""
1、常见文件读取方式
2、Dataframe 常见属性方法
3、掌握常见基础时间处理方式
4、分组聚合原理
5、掌握交叉表和透视表
"""
"""==============================基础语法============================="""
# 1、文本数据：.txt/.csv
# .csv 典型的一种分隔符文件，默认分隔符是','
info = pd.read_csv('./meal_order_info.csv', encoding='gbk')
print(info)

detail = pd.read_excel('./meal_order_detail.xlsx', sheetname=1)
# print(detail)

"""================创建dataframe======================="""
data_dic = {'姓名': ['x1', 'y1', 'z1'], '年龄': [12, 13, 15]}
df1 = pd.DataFrame(data_dic)
print(df1)

# 通过参数传值
import numpy as np

# data = np.array([['x1',21],['y1',23],['z1',21]])
data = [['x1', 21], ['y1', 23], ['z1', 21]]
columns = np.array(['姓名', '年龄'])
df2 = pd.DataFrame(data=data, columns=columns)
print(df2)

# 3、dataframe 属性
print('dataframe元素类型:\n', type(df2.values))
print('dataframe元素:\n', df2.values)
print('dataframe行索引:\n', df2.index)
print('dataframe的列索引:\n', df2.columns)
print('dataframe元素类型：\n', df2.dtypes)
print('dataframe转置：\n', df2.T)  # 行索引、列索引互换

# 4、查询数据
print(type(df2['姓名']))  # series类型  表示是一列数据，只有行索引，没有列索引 q
print('姓名：\n', df2['姓名'])

# 5、创建series类型方法
data = ['a', 'b', 'c']
ser1 = pd.Series(data=data)
print('ser1:\n', ser1)

# 6、DataFrame 访问
# 一、切片
print(df2[['年龄', '姓名'][:2]])
print(df2[:][:2])

# 二、获取多行多列
# head()默认是前5行   tail()默认是后5行

# 方法三：loc和iloc
"""
df.loc[行索引名称或条件,列索引名称]
df.iloc[行索引位置,列索引位置]
"""
print('============')
print('loc:\n', df2.loc[:2, '姓名'])  # 前闭后闭

# iloc
print('iloc:\n', df2.iloc[0:2, 0])  # 前闭后开

# 条件切片   order_id = 412的菜
print(detail.loc[detail['order_id'] == 412, 'dishes_name'])

mask1 = detail['dishes_name'] == '白饭/大碗'
mask2 = detail['dishes_name'] == '白饭/小碗'
mask = mask1 | mask2
print(detail.loc[mask, 'order_id'])
print('====================================================')
# 方法二：通过np.any()求bool
# np.any(mask1, mask2)
# arr = np.vstack((mask1, mask2))
# mask = np.any(arr, axis=0)

# 条件切片
print(detail.loc[mask, 'order_id'])

# 更改DataFrame中的数据
detail.loc[detail['order_id'] == 1132, 'order_id'] = 113
print(detail.loc[detail['order_id'] == 1132, 'order_id'])

# 增加数据
detail['payment'] = detail['amounts'] * detail['counts']
print(detail['payment'])

# 删除某一列数据
detail.drop(labels='payment', inplace=True, axis=1)  # labels 列索引名称  axis=1 删除列宽度变窄

# DataFrame统计描述
"""
np.median()中位数
np.cov() 协方差
np.ptp() 极差
"""
print(detail['amounts'].mean())

"""
pandas  统计方法
counts  非空数目
mode    众数
value_counts  类别数
"""
print(detail['dishes_name'].value_counts())

"""
count    3647.000000
mean        1.110502
std         0.610403
min         1.000000
25%         1.000000
50%         1.000000
75%         1.000000
max        10.000000
"""
print(detail['counts'].describe())
# 将数值型转化为类别型数据
detail['amount'] = detail['counts'].astype('category')
print(detail['amount'].describe())
"""
count      3647
unique      152    （去重之后的个数）
top       白饭/大碗（出现次数最多的种类名称）
freq        122  (出现次数最多的种类频率)
"""
print(detail['dishes_name'].describe())
