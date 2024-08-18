#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 11、责任链模式.py
@Time: 2020/5/16 22:00
@user：liuhuan   
"""

"""
责任链(Chain of Responsibility)模式用于让多个对象来处理单个请求时，或者用于预先不知道应该由哪个对象（来自某个对象链）来处理某个特定请求时。原则如下：
    ① 存在一个对象链（链表、树或任何其他便捷的数据结构）。
    ② 我们一开始将请求发送给链中的第一个对象。
    ③ 对象决定其是否要处理该请求。
    ④ 对象将请求转发给下一个对象。
    ⑤ 重复该过程，直到到达链尾。

注意：
    客户端代码仅知道第一个要处理的元素，而非拥有对其所有元素的引用，并且每一个处理元素仅知道其直接的下一个邻居(称为后继)，而不知道所有其他处理的元素。也被称为：单向链表。

责任链模式可以参考生活中的ATM机槽口：
    可以放入：100,50,20,10,5,1,。槽口接收完钱之后由不同的容器对比。钞票返回时则是从适当的容器中取。
"""


# Event类描述一个事件
class Event():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Widget是一个核心应用类
class Widget:
    def __init__(self,parent=None):
        self.parent = parent

    # 动态分发，通过hasattr和getattr决定请求由谁处理
    def handle(self,event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, "handle_default"):
            self.handle_default(event)


#  具有不同行为的控件,处理close和defalut事件
class MAinWindow(Widget):
    def handle_close(self, event):
        print("MianWindow：{}".format(event))

    def handle_default(self,event):
        print("MainWindow Default：{}".format(event))


# 处理paint事件
class SenDialog(Widget):
    def handle_paint(self, event):
        print("SenDialog：{}".format(event))


# 处理down事件
class MsgText(Widget):
    def handle_down(self,event):
        print("MsgText：{}".format(event))


# main函数展示创建控件和事件，以及控件如何对事件做出反应
def main():
    mw = MAinWindow()
    sd = SenDialog(mw)
    msg = MsgText(sd)
    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)

if __name__ == '__main__':
    main()
