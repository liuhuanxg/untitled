def func1(list1):
    new_list = []
    for i in list1:
        if type(i) == list:
            new_list.extend(func1(i))
        else:
            new_list.append(i)
    return new_list


lst = [1, 2,[3, 4, [5, [6], 7, [8, 9]]]]
print(func1(lst))