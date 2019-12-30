"""
基本思想：在要排序的一组数中，选出最小（或最大）的一个数与第一个位置的数交换；然后在剩下的数当中再找最小（或者最大）的与第2个位置的数交换，依次类推，直到第n-1个元素（倒数第二个数）和第n个元素（最后一个元素）比较为止。时间复杂度：On2
"""

list1=[9,6,8,4,7]

print(list(filter(lambda x:True if x%2==1 else False ,list1)))
def select_sort(alist):

    '''
    :param alist: 将要排序的列表
    :return: 排序完之后返回的列表
    '''
    n=len(alist)
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾位置选择出最小数据
        for j in range(i+1,n):
            if alist[j]<alist[min_index]:
                min_index = j
        #如果选择出的数据不在正确的位置，进行交换
        if min_index!=i:
            alist[i],alist[min_index]=alist[min_index],alist[i]
        print(alist)
select_sort(list1)
