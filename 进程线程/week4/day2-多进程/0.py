def func1(name):
    print("name1", name)
    return name


def func2(name):
    print("name2", name)


class Func():
    def __init__(self, func, *args, callback=None):
        self.func = func
        self.args = args
        self.callback = callback

    def start(self):
        ret = self.func(self.args[0])
        if self.callback:
            self.callback(ret[0])


f = Func(func1, ("哪吒",), callback=func2)
f.start()
