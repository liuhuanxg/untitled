#现有两个从小到大排好序的 int 数组（每个数组自身没有重复元素）。请找出所有在 这两个数组中都出现过的数。请写一个函数，输入为两个数组。

def choice(list1,list2):
    print(list(set(list1)&set(list2)))

if __name__ == '__main__':
    list1=eval(input('请输入第一个列表：'))
    list2=eval(input('请输入第二个列表：'))
    choice(list1,list2)