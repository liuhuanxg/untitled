"""
清洗 sheetname=0
1.求该饭店除了米饭以外，什么菜卖的最好？
2.清洗表：要求剔除整列为空的列；剔除元素取值完全相同的列
3.哪个订单下的物品最多？
"""
import pandas as pd

detail = pd.read_excel('./meal_order_detail.xlsx', sheetname=0)
# print('columns:\n', detail.columns)
# print('values:\n', detail.values)

"""1、第一种方法(先将米饭进行删除)"""
# mask1 = detail['dishes_name'] == '白饭/大碗'
# mask2 = detail['dishes_name'] == '白饭/小碗'
# mask = mask1 | mask2
# order = detail.loc[mask, :].index   # 获取米饭的索引
#
# print(detail.shape)
# detail.drop(labels=order, inplace=True, axis=0)
# print(detail.shape)
# print(detail['dishes_name'].mode())  # 提取众数

"""第二种方法"""
# print(detail['dishes_name'].value_counts()[1:2])


# 2、
columns = detail.columns

drop_list = []
for column in columns:
    # 进行去重
    res = detail.drop_duplicates(subset=column, inplace=False)
    if res.shape[0] == 1:
        # 认为这一列所有数据一样  不管是NA还是1、0
        drop_list.append(column)

# print(drop_list)
detail.drop(labels=drop_list, axis=1, inplace=True)
# print(detail.shape)

"""3-"""
print(detail['order_id'].value_counts()[0:1].index)
print(detail['order_id'].mode())