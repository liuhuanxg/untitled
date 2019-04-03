# def quickSort(arr):
#     if len(arr)<=1:
#         return arr
#     m=arr[len(arr)//2]
#     left=[x for x in arr if x<m]
#     right=[x for x in arr if x>m]
#     mm=[x for x in arr if x==m]
#     return quickSort(left)+mm+quickSort(right)
#
# if __name__ == '__main__':
#     arr=[8,5,3,6,4,9]
#     print(quickSort(arr))

#quick sort
def quickSort(array):
    if len(array) < 2:
        return array
    else:
        baseValue = array[0]
        less = [m for m in array[1:] if m < baseValue]
        equal = [w for w in array if w == baseValue]
        greater = [n for n in array[1:] if n > baseValue]
    return quickSort(less) + equal + quickSort(greater)
array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quickSort(array))



if __name__ == '__main__':
    ar=[8,7,52,3,1,4]
    print(quickSort(ar))
