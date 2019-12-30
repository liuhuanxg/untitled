# total=float(input('请输入购物金额：'))
# if total >= 500:
#     sex=input('请输入性别：')
#     if sex == '男':
#         print('赠送您刮胡刀')
#     elif sex == '女':
#         print('赠送您化妆品')
# else:
#     sex=input('请输入性别：')
#     if sex == '男':
#         print('赠送您打火机')
#     elif sex == '女':
#         print('赠送您发卡')

price=float(input('请输入西红柿单价：'))
num=float(input('请输入购买数量：'))
total=price*num
if total>=50:
    level=input('请输入vip级别：')
    if level == '1':
        total *= 0.8
        print('享受总金额打八折优惠，金额为：%.2f' % total)
    elif level == '2':
        total=int(total)
        total=total-total%10
        print('享受抹零优惠，金额为：%d' % total)
    elif level == '3':
        print('享受去小数优惠，金额为：%d' % total)
else:
    sex=input('请输入性别:')
    if sex == '男':
        print('赠送玩具劳斯莱斯一个')
    elif sex == '女':
        print('赠送小猫一只')