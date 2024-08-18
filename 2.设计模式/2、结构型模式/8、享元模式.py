#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 8、享元模式.py
@Time: 2020/5/16 20:58
@user：liuhuan   
"""

"""
享元模式：通过为相似对象引入数据共享来最小化内存使用，提升性能。
一个享元（Flyweight）就是一个包含状态独立的不可变（又称固有的）数据的共享对象，依赖状态的可变（又称非固有的）数据不应是享元的一部分，因为每个对象的这种信息不同，无法共享。如果享元需要非固有数据，应该由客户端代码显示地提供。

示例：
    在设计游戏中，两个团队的所有士兵都有一些共同的数据，比如，挑起、低头等，这些数据可以创建一个享元来包含所有共有的数据。
    士兵也有一些因人而异的数据，比如强制，健康状态等，这些数据不是共享的一部分
    
享元旨在优化性能和内存使用。所有嵌入式系统（手机、平板电脑等）和性能关键的应用（游戏、3D图形处理和实时系统等）都能从中获益

使用享元模式的条件：
    ·应用需要使用大量的对象
    ·对象太多，存储/渲染他们的代价太大。一旦移除对象中的可变状态，多组不同的对象可被相对更少的共享对象所替代。
    ·对象ID对于应用不重要。对象共享会造成ID比较的失败，所以不能依赖对象ID
"""




import random
from enum import Enum
TreeType = Enum("TreeType","apple_tree cherry_tree peach_tree")

class Tree:
    pool = dict()
    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print("render a tree of type {} and age {} at ({},{})".format(self.tree_type, age, x, y))

def main():
    rnd = random.Random()
    age_min, age_max = 1, 30  #单位为年
    min_point, max_point = 0, 100
    tree_counter = 0
    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1
    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1

    print("trees rendered:{}".format(tree_counter))
    print("trees actually created:{}".format(len(Tree.pool)))
    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print("{} == {}? {}".format(id(t4), id(t5), id(t4) == id(t5)))
    print("{} == {}? {}".format(id(t5), id(t6), id(t5) == id(t6)))

if __name__ == '__main__':
    main()

