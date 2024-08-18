class Animal():
    def __init__(self):
        self._initialized = True

    @property
    def name(self):
        assert self._initialized, "Thread.__init__() not called"
        return "this is Animal"

    @name.setter
    def name(self, name):
        assert self._initialized, "Thread.__init__() not called"
        self._name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name


d = Dog("藏獒")
print(d.name)
print(Animal.name)
