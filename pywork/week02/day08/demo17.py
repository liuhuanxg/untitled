# 返回时间戳 从19701月1日00:00:00开始到现在的秒数，float类型
import time
# print(time.time())
# time.sleep(3)
# print(time.time())

# 获取时间元组,可接受时间戳参数
# ret=time.localtime()
# print(ret)
# print(time.localtime(time.time()-3600))    # tm_hour-1

# 时间字符串格式化
s=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
print(s,type(s))
# 时间元组转换为字符串
s=time.strftime('%Y/%m/%d %H-%M-%S',time.localtime())
print(s,type(s))
# 字符串转换为时间元组 差8小时
t=time.strptime(s,'%Y/%m/%d %H-%M-%S')
print(t)
t=time.localtime(time.time())
print(t)
# 时间元组转换为时间戳
x=time.mktime(t)
print(x)

# UTC--国际协调时间，比北京时间少8小时
# s=time.gmtime()
# print(s)

t=time.time()
s=time.localtime()
print(s)
f=time.strftime('%Y-%m-%d %H:%M:%S',s)
print(f)
p=time.strptime(f,'%Y-%m-%d %H:%M:%S')
print(p)
t=time.mktime(p)
print(t)