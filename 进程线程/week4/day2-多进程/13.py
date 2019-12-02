def print_num(num):
    print(num)
    if num==1:
        return
    num=num-1
    print_num(num)
    print('-----》')
print_num(3)