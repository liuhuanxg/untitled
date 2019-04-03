
# 表示：将迭代器当中的元素，依次作用在函数当中
# map(函数名，迭代器)

def my_sq(num):
    return num**2

temp_list = [i for i in range(1,11)]#[1,2,3,4,....10]
# result_list = []
# for value in temp_list:
#     new_value = my_sq(value)
#     result_list.append(new_value)
#
# print(result_list)

result = list(map(my_sq,temp_list))
print(result)