class Phone():
    def __phone(self):
        print('正在拨打电话')
    def phone(self,m):
        if m >=30:
            self.__phone()
        else:
            print('请先交费30元，再打电话')
x=Phone()
x.phone(36)