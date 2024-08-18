#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 9.py
@Time: 2020/5/16 21:54
@user：liuhuan   
"""
"""
关注点分离（Separation of Concerns,SoC）原则是软件工程相关的设计原则之一。SoC原则背后的思想是将一个应用且分为不同的部分，每个部分解决一个单独的关注点。

模型-视图-控制器（Model-View-Controller，MVC）模式是应用到面向对象编程的SoC原则。

模型是核心，代表应用的信息本院，包含和管理（业务）逻辑、数据、状态以及应用的规则。视图是模型的可视化表现，只展示数据，并不处理数据。控制器是模型与视图之间的链接/粘附。模型与视图之间的所有通信东通过控制器进行。

示例：
    用户输入数字，然后就能看到与数字相关的，名人名言。名人名言存储在quotes元组中，通常这些数据存储在数据库、文件或其他地方只有模型能够直接访问。
    
"""

quotes = ("A man is not complete until he is married.Then he is finished..",
          'As I said before, I never repeat myself.',
            'Behind a successful man is an exhausted woman.',
            'Black holes really suck...', 'Facts are stubborn things.'
          )

# 模型
class QuoteModel():

    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = "Not found!"
        return value


#视图
class QuoteTerminalView:

    def show(self,quote):
        print("And the quote is:'{}'".format(quote))

    def error(self,msg):
        print("Error:{}".format(msg))

    def select_quote(self):
        return  input("请选择一个选项：")


# 控制器
class QuoteTerminalController():

    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
            else:
                valid_input = True
        quote = self.model.get_quote(n)
        self.view.show(quote)


# 启动函数
def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ =="__main__":
    main()