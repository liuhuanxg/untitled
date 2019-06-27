#1、python语言有什么特点？

#2、列举所知道的排序算法，并实现一个

#3、介绍一下Python中的可变参数与关键字参数？

#4、下边的代码会输出什么？

def f(x,l=[]):
    for i in range(x):
        l.append((i*i))
    print(l)
f(2)  #[0, 1]
f(3,[3,2,1])   #[3, 2, 1, 0, 1, 4]
f(3)    #[0, 1, 0, 1, 4]

#5、下边这些是什么意思？@classmethod,@staticmethod,@property

#6、编程：输入一个字符串，输出该字符串中字符的所有组合

#例：输入123，输出为：1,2,3,12,13,23,123

#7、谈谈你所知的python web 框架

#8、使用Python将数据库student表中提取的数据写入db.txt

#9、编程实现斐波那契数列（使用递归）

#10、简述left join 和right join的区别？
