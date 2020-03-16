#每次将一个数插入到有序数列的相应位置，插入之后原有序序列依然有序，只是长度加1
def insertionSort(lyst):
    for i in range(1,len(lyst)):
        j = i-1
        item = lyst[i]
        while  j >= 0:
            if lyst[j] > item:
                lyst[j+1] = lyst[j]
            else:
                break
            j -= 1
        lyst[j+1] = item
    return lyst
if __name__ == '__main__':
    items = [8, 9, 7, 10, 5, 3, 4]
    re = insertionSort(items)
    print(re)