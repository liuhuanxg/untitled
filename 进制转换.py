def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        basevalue=arr[0]
        left=[i for i in arr[1:] if i<basevalue]
        common=[j for j in arr if j==basevalue]
        right=[k for k in arr[1:] if k>basevalue]
    return quicksort(left)+common+quicksort(right)

if __name__ == '__main__':
    list1=[8,3,1,9,3,5,7]
    print(quicksort(list1))

class Father():
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super(Father,cls).__new__(cls,*args,**kwargs)
        return cls._instance
class Foo(Father):
    pass

f1=Foo()
f2=Foo()
print(f1 is f2)
