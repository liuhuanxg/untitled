class Single(object):
    __instance = None
    def __new__(cls):
        # super().__new__(cls)
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

s = Single()
print(id(s))

b = Single()
print(id(b))
