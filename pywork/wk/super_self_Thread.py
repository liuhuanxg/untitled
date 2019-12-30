import threading, time
class Sing(threading.Thread):
    def __init__(self, name):
        self.name = name
        super(Sing, self).__init__()

    def run(self) -> None:
        for i in range(3):
            print(self.name, "唱歌{}".format(i + 1))
            time.sleep(1)
class Dance(threading.Thread):
    def __init__(self, q, name):
        super(Dance, self).__init__()
        self.name = name
        self.q = q
    def run(self) -> None:
        for i in range(3):
            print(self.name, "跳舞{}".format(i + 1))
            time.sleep(1)
def main():
    s = Sing("李四")
    d = Dance(1, "张三")
    s.start()
    d.start()
if __name__ == '__main__':
    main()