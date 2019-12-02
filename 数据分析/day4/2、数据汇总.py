import pandas as pd
from pandas import DataFrame
import xlrd

wb=xlrd.open_workbook('zhongduan.xlsx')
sheets=wb.sheet_names()
print(sheets)

#汇总整个月份数据
total=DataFrame()
for i in range(len(sheets)):
    df=pd.read_excel('zhongduan.xlsx',sheet_name=sheets[i],skiprows=0,index=False,encoding='utf8')
    total=total.append(df)

print('总共有：',total.shape)

#保存到一个工作表中
writer=pd.ExcelWriter('output1.xlsx')
total.to_excel(writer,sheet_name='Sheet1')
writer.save()