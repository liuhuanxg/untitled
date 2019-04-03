
while True:
    with open('zhanghu.txt','w')as f:
        name = input('请创建用户名：')
        ai = []
        mima = input('请输入密码:')
        cd = len(mima)
        j = 0
        xhx = 0
        if mima[cd - 2] != '@':
            print('密码倒数第二个字符不是@')
            continue
        while j < cd:
            if mima[j] == '_':
                xhx += 1
            j += 1
        if xhx == 0:
            print('没有下划线。')
            continue
        print('密码设置正确。')
        money = float(input('请输入存款金额：'))
        ai.append(name)
        ai.append(mima)
        ai.append(money)
        f.write(str(ai))
        f.write('\n')
    break
    # print(ai)
with open ('zhanghu.txt','r+')as f:
    line=f.readline
    dlname=input('请输入用户名字：')
    if ai[0]==dlname:
        j=3
        while j>0:
            print('您有%d次机会输入密码'%j)
            dlmima=input('请输入用户密码：')
            if j>1:
                if ai[1]!=dlmima:
                    print('密码输入错误，你还有%d次机会'%(j-1))
                elif ai[1]==dlmima:
                    cq=int(input('密码输入正确，请选择要进行的操作：3、存钱。4、取钱'))
                    if cq==3:
                        cunqian = float(input('请输入存钱金额：'))
                        ai[2] += cunqian
                        print(ai)
                        f.write(str(ai))
                        break
                    elif cq==4:
                        while True:
                            quqian = float(input('请输入取款金额：'))
                            if quqian > ai[2]:
                                print('您的取款金额超出了账户金额,请重新输入金额：')
                                continue
                            else:
                                ai[2] -= quqian
                                print(ai)
                                f.write(str(ai))
                        break
            elif j==1:
                if ai[1] != dlmima:
                    print('密码输入错误，银行卡被冻结')
                    break
                elif ai[1] == dlmima:
                    cq = int(input('密码输入正确，请选择要进行的操作：3、存钱。4、取钱'))
                    if cq == 3:
                        cunqian = float(input('请输入存钱金额：'))
                        ai[2] += cunqian
                        print(ai)
                        f.write(str(ai))
                        break
                    elif cq == 4:
                        while True:
                            quqian = float(input('请输入取款金额：'))
                            if quqian > ai[2]:
                                print('您的取款金额超出了账户金额,请重新输入金额：')
                                continue
                            else:
                                ai[2] -= quqian
                                print(ai)
                                f.write(str(ai))
                    break
            j -= 1
    else:
         print('用户名输入错误，请重新输入。')

