class Denglu():
  def denglu(self):
    with open('zhanghu.txt', 'r+')as f:
        line = f.readline()
        list=eval(line)
        dlname = input('请输入用户名字：')
        if list[0] == dlname:
            j = 3
            while j > 0:
                print('您有%d次机会输入密码' % j)
                dlmima = input('请输入用户密码：')
                if j > 1:
                    if list[1] != dlmima:
                        print('密码输入错误，你还有%d次机会' % (j - 1))
                    elif list[1] == dlmima:
                        cq = int(input('密码输入正确，请选择要进行的操作：3、存钱。4、取钱'))
                        if cq == 3:
                            cunqian = float(input('请输入存钱金额：'))
                            list[2] += cunqian
                            print(list)
                            f.write(str(list))
                            break
                        elif cq == 4:
                            while True:
                                quqian = float(input('请输入取款金额：'))
                                if quqian > list[2]:
                                    print('您的取款金额超出了账户金额,请重新输入金额：')
                                    continue
                                else:
                                    list[2] -= quqian
                                    print(list)
                                    f.write(str(list))
                            break
                elif j == 1:
                    if list[1] != dlmima:
                        print('密码输入错误，银行卡被冻结')
                        break
                    elif list[1] == dlmima:
                        cq = int(input('密码输入正确，请选择要进行的操作：3、存钱。4、取钱'))
                        if cq == 3:
                            cunqian = float(input('请输入存钱金额：'))
                            liste[2] += cunqian
                            print(list)
                            f.write(str(list))
                            break
                        elif cq == 4:
                            while True:
                                quqian = float(input('请输入取款金额：'))
                                if quqian > list[2]:
                                    print('您的取款金额超出了账户金额,请重新输入金额：')
                                    continue
                                else:
                                    list[2] -= quqian
                                    print(list)
                                    f.write(str(list))
                        break
                j -= 1
        else:
            print('用户名输入错误，请重新输入。')