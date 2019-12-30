def hs():
    print('我在函数内')
if __name__=='__main__':
    print('我在函数外')
else:
    print('我不是主函数，我是',__name__)
print(globals())