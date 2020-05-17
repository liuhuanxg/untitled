#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 8、享元模式.py
@Time: 2020/5/16 20:58
@user：liuhuan   
"""

"""
运用共享技术有效地支持大量细粒度的对象
内部状态：享元对象中不会随环境改变而改变的共享部分，比如围棋妻子的颜色
外部状态：随环境改变而改变、不可以共享的状态就是外部状态。比如围棋棋子的位置。

应用场景：程序中使用了大量的对象，如果删除了对象的内部状态，可以用相对较少的共享对象取代很多组对象
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

