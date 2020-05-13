#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo.py
@Time: 2020/5/12 10:25
@user：liuhuan   
"""
def  reverseMergeSortArray(a,b):
    len_a = len(a)-1
    len_b = len(b)-1
    new_list = []
    while len_a>=0 and len_b>=0:
        if a[len_a] < b[len_b]:
            new_list.append(b[len_b])
            len_b -= 1
        elif a[len_a] > b[len_b]:
            new_list.append(a[len_a])
            len_a -= 1
        elif a[len_a] == b[len_b]:
            new_list.extend([a[len_a],b[len_b]])
            len_a -= 1
            len_b -= 1
    if len_a < 0:
        new_list.extend(b[0:len_b+1])
    elif len_b < 0:
        new_list.extend(a[0:len_a + 1])
    return new_list


a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6, 7]
print(reverseMergeSortArray(a, b))


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: List
        :type l2: List
        :rtype: List
        """
        l1 = list(reversed(l1))
        l2 = list(reversed(l2))
        l1, l2 = self.judgeLen(l1, l2)
        print(l1, l2)
        add_nums = []
        for i in range(len(l1)):
            add_num, flag = self.judgeCarry(l1[i], l2[i])
            if flag == 0:
                add_nums.append(add_num)
            else:
                add_nums.append(add_num)
                try:
                    l1[i + 1] = l1[i + 1] + 1
                except:
                    continue
        if add_nums[-1] == 0:
            add_nums.append(1)
        print(list(reversed(add_nums)))

    def judgeCarry(self, a, b):
        if a + b > 9:
            return [(a + b) % 10, 1]
        else:
            return [a + b, 0]

    def judgeLen(self, l1, l2):
        lenl1 = len(l1)
        lenl2 = len(l2)
        add_len = []
        for i in range(abs(lenl2 - lenl1)):
            add_len.append(0)
        if lenl1 >= lenl2:
            for i in range(abs(lenl2 - lenl1)):
                l2.append(0)
            # print([l1,add_len])
            return [l1, l2]
        else:
            for i in range(abs(lenl2 - lenl1)):
                l1.append(0)
            add_len.append(l1)
            # print([l2,add_len])
            return [l2, l1]


if __name__ == '__main__':
    S = Solution()
    S.addTwoNumbers([2, 4, 3, 5, 6, 4, 7, 4], [5, 6, 4, 4, 5, 6, 7])

