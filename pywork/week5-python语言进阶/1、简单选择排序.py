"""
1、数据结构和算法
算法：解决问题的方法和步骤
评价算法优劣：渐进时间复杂度和渐进空间复杂度
渐近时间复杂度的大O标记：
O(c)——常亮时间复杂度——布隆过滤器、哈希存储
O(log2n)——对数时间复杂度——折半查找（二分查找）
O(n)——线性时间复杂度——顺序查找/桶排序
O(n*log2n)——对数线性时间复杂度——高级排序算法(归并排序、快速排序)
O(n2)——平方时间复杂度——简单排序算法(选择排序、插入排序、冒泡排序)
o(n3)——立方时间复杂度——Floyd算法/矩阵乘法运算
O(2n)——几何级数时间复杂度——汉诺塔
O(n!)——阶乘时间复杂度——旅行经销商问题—NP
"""

# 排序算法（选择、冒泡和归并）和查找算法（顺序和折半）
def select_sort(origin_items,comp=lambda x,y:x<y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items)-1):
        min_index=i
        for j in range(i+1,len(items)):
            if comp(items[j], items[min_index]):
                min_index=j
        items[i],items[min_index] = items[min_index],items[i]
        print("items:",items)
    return items

if __name__=="__main__":
    items=[8,9,7,11,5,10,4]
    re=select_sort(items)
    print(re)