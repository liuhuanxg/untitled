#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 5、适配器模式.py
@Time: 2020/5/15 22:48
@user：liuhuan   
"""
"""
所谓适配器模式是指一种接口适配技术，它可通过某个类来使用另一个接口与之不兼容的类，运用此模式，两个类的接口都无需改动

适配器模式主要用于希望复用一些现存的类，但是接口又与复用环境要求不一致的情况，比如在需要对早起代码复用一些功能等应用上很有实际价值

解释二：
    适配器模式(Adapter Pattern)：将一个类的接口转换成为客户希望的另外一个接口.Adapter Pattern是的原本由于接口不兼容而不能一起工作的那些类可以一起工作。
    应用场景：系统数据和行为都正确，但接口不符合时，目的是使控制外围之外的一个原有对象与某个接口匹配，适配器模式主要应用于希望复用一些现存的类，但接口又与复用环境不一致的情况
    
    
"""
class Target(object):
    def request(self):
        print("普通请求")

class Adaptee(object):
    def specific_request(self):
        print("特殊请求")

class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()
    def request(self):
        self.adaptee.specific_request()

if __name__ == '__main__':
    target = Adapter()
    target.request()