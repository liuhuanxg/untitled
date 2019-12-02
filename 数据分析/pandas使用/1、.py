import numpy as np
import pandas as pd

#创建一个Series通过传递值的列表，创建一个默认的证书索引：
# list1 = [1,3,5,np.nan,6,8]
# s = pd.Series(list1)
# print(s)

# DataFrame通过传递带有日期时间索引和带标签的列的Numpy数组来川港一个：
dates = pd.date_range('20130101',periods=6)
print("dates:",dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
print("df",df)

#DataFrame通过传递对象的字典来创建，这些对象可以转换为类似序列的对象
df2 = pd.DataFrame({
    "A":1,
    "B":pd.Timestamp('20130102'),
    "C":pd.Series(1,index=list(range(4)),dtype='float32'),
    "D":np.array([3]*4,dtype='int32'),
    "E":pd.Categorical(["test","train","test","train"]),
    "F":"foo"
                    })
print("df2:",df2)
print("df2type：",df2.dtypes)
