
import pandas as pd
#读取文件
order = pd.read_table('meal_order_info.csv',sep=',',encoding='gbk')
print(order)

#1.将字符串时间转换成标准时间
print('原始状态：',order['lock_time'].dtypes)#object

order['lock_time'] = pd.to_datetime(order['lock_time'])
print('转换化：',order['lock_time'].dtypes)

# 2.查看Timestamp类型的时间限制
print('最小时间：',pd.Timestamp.min)#1677-09-21 00:12:43.145225
print('最大时间：',pd.Timestamp.max)#2262-04-11 23:47:16.854775807

#3.
dateIndex = pd.DatetimeIndex(order['lock_time'])
print('转换为DatetimeIndex后数据的类型：',type(dateIndex))
print(dateIndex)

#4.获取lock_time前5个数据，而且只要年，其它的不要
years = [i.year for i in order['lock_time']]
print('前5条（年）：',years[:5])
months = [i.month for i in order['lock_time']]
print('前5条(月)：',months[:5])
days = [i.day for i in order['lock_time']]
print('前5条(天)：',days[:5])

weekdays = [i.weekday_name for i in order['lock_time']]
print('前5条(星期)：',weekdays[:5])

#将lock_time数据向后平移一天
time_1 = order['lock_time']+pd.Timedelta(days=1)
print('lock_time在加上1天（前5条）的数据为：',time_1[:5])


#输出lock_time减去2017.1.1.0：0：0分的数据
time_2 = order['lock_time'] - pd.to_datetime('2017-1-1 0:0:0')
print('lock_time减去2017.1.1.0：0：0分的数据:',time_2[:5])




#点餐用时最少和最多的时间是多少
order['use_start_time']=pd.to_datetime(order['use_start_time'])
checkTime=order['lock_time']-order['use_start_time']
print('最少点餐时间为：',checkTime.min())
print('最多点餐时间为：',checkTime.max())
print('平均点餐用时为：',checkTime.mean())

#作业：求每天的点餐用时最少、最多、平均时间