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


# #-*-coding:utf-8 -*-
# """
# @project:untitled
# @File: demo.py
# @Time: 2020/5/12 10:25
# @user：liuhuan
# """
# def  reverseMergeSortArray(a,b):
#     len_a = len(a)-1
#     len_b = len(b)-1
#     new_list = []
#     while len_a>=0 and len_b>=0:
#         if a[len_a] < b[len_b]:
#             new_list.append(b[len_b])
#             len_b -= 1
#         elif a[len_a] > b[len_b]:
#             new_list.append(a[len_a])
#             len_a -= 1
#         elif a[len_a] == b[len_b]:
#             new_list.extend([a[len_a],b[len_b]])
#             len_a -= 1
#             len_b -= 1
#     if len_a < 0:
#         new_list.extend(b[0:len_b+1])
#     elif len_b < 0:
#         new_list.extend(a[0:len_a + 1])
#     return new_list
#
#
# a = [1, 2, 3, 4, 5]
# b = [2, 3, 4, 5, 6, 7]
# print(reverseMergeSortArray(a, b))
#
#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: List
#         :type l2: List
#         :rtype: List
#         """
#         l1 = list(reversed(l1))
#         l2 = list(reversed(l2))
#         l1, l2 = self.judgeLen(l1, l2)
#         print(l1, l2)
#         add_nums = []
#         for i in range(len(l1)):
#             add_num, flag = self.judgeCarry(l1[i], l2[i])
#             if flag == 0:
#                 add_nums.append(add_num)
#             else:
#                 add_nums.append(add_num)
#                 try:
#                     l1[i + 1] = l1[i + 1] + 1
#                 except:
#                     continue
#         if add_nums[-1] == 0:
#             add_nums.append(1)
#         print(list(reversed(add_nums)))
#
#     def judgeCarry(self, a, b):
#         if a + b > 9:
#             return [(a + b) % 10, 1]
#         else:
#             return [a + b, 0]
#
#     def judgeLen(self, l1, l2):
#         lenl1 = len(l1)
#         lenl2 = len(l2)
#         add_len = []
#         for i in range(abs(lenl2 - lenl1)):
#             add_len.append(0)
#         if lenl1 >= lenl2:
#             for i in range(abs(lenl2 - lenl1)):
#                 l2.append(0)
#             # print([l1,add_len])
#             return [l1, l2]
#         else:
#             for i in range(abs(lenl2 - lenl1)):
#                 l1.append(0)
#             add_len.append(l1)
#             # print([l2,add_len])
#             return [l2, l1]
#
#
# if __name__ == '__main__':
#     S = Solution()
#     S.addTwoNumbers([2, 4, 3, 5, 6, 4, 7, 4], [5, 6, 4, 4, 5, 6, 7])
#
