import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np


# 数据
data=ts.get_k_data('600728',start='2018-10-15',end='',ktype='D')
print(data)
prices=data[['open','high','low','close']]
dates=data['date']
n=list(range(len(dates)))
candleData=np.column_stack((n,prices))
print(candleData)

#创建画布
fig=plt.figure()
#添加轴
# myax=fig.add_axes([0.1,0.3,0.8,0.6])  #下午讲数据含义
#
# mpf.candlestick_ohlc(ax=myax,quotes=candleData,width=0.5,colorup='r',colordown='g')
# plt.show()