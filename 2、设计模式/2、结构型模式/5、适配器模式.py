#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 5、适配器模式.py
@Time: 2020/5/15 22:48
@user：liuhuan   
"""
"""
适配器模式（Adapter pattern）是一种结构型设计模式，帮助我们实现两个不兼容接口之间
的兼容。首先，解释一下不兼容接口的真正含义。如果我们希望把一个老组件用于一个新系统中，
或者把一个新组件用于一个老系统中，不对代码进行任何修改两者就能够通信的情况很少见。但
又并非总是能修改代码，或因为我们无法访问这些代码（例如，组件以外部库的方式提供），或
因为修改代码本身就不切实际。在这些情况下，我们可以编写一个额外的代码层，该代码层包含
让两个接口之间能够通信需要进行的所有修改。这个代码层就叫适配器。
    
"""

# 首先是我们有什么？
class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'

# 接着是想要什么
class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "the {} synthesizer".format(self.name)

    def play(self):
        return "is playing an electronic song"

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{} the human".format(self.name)

    def speak(self):
        return "says hello"


"""
这时客户端仅知道如何调用execute()方法，并不知道play()和speak()，
在不改变Synthesizer和Human类的前提下，该如何使代码更有效？
"""

# 建造适配器
class Adapter():
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


# 使用适配器
def main():
    objects = [Computer("Asus")]
    synth = Synthesizer("moog")
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human("Bob")
    objects.append(Adapter(human,dict(execute=human.speak)))

    for i in objects:
        print("{} {}".format(str(i), i.execute()))

if __name__ == '__main__':
    main()