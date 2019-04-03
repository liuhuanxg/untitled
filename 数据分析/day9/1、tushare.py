import tushare as ts
import pandas as pd
import numpy as np

#内容太大时，强制显示所有内容，不省略
np.set_printoptions(threshold=np.NaN)

pd.set_option('display.max_columns',None)
#显示所有行
pd.set_option('display.max_rows',None)
#设置value的显示长度为100，默认为50

data=ts.get_hist_data('300274',start='2018-03-01',end='2018-03-27')
print(data)

# data=ts.get_h_data('300274')
# print(data)

