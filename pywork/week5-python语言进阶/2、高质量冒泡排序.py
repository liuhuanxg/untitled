# 冒泡排序第一次排完之后，最大的数一定在最后边
def bubble_sort(origin_items,comp=lambda x,y:x>y):
    """高质量冒泡排序（搅拌排序）"""
    items = origin_items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i,len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) -2 -i ,i,-1):
                if comp(items[j-1],items[j]):
                    items[j],items[j-1]=items[j-1],items[j]
                    swapped = True
        if not swapped:
            break
    return items

if __name__=="__main__":
    items=[8,9,7,3,5,4,10]
    re=bubble_sort(items)
    print(re)