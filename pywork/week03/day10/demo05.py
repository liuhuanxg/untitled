class Phone():
    def test(self):
        print('test1')
    def __test1(self):
        print('test1')
x=Phone()
x.test()

# 私有方法，无法调用
x.__test1()    # 'Phone' object has no attribute '__test' bbbbbbbbbbbb