def func1(func):
    print("111111111111")
    def inner():
        print("333333333333")
        func()
        print("444444444444")
        return "OK"
    return  inner

def func3(func):
    print("55555555555")
    def inner():
        print("777777777777")
        func()
        print("888888888888")
        return "python"
    return inner

@func1
@func3
def func2():
    print("222222222222")
    return  "js"
print(func2())