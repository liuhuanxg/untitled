str1=3+4j
print(str1,type(str1))   #(3+4j) <class 'complex'>

str1 = "hello world!"
print(str1,type(str1))  #hello world! <class 'str'>

print(dir(str1))
#[ 'capitalize', 'casefold', 'center', 'count', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

list1 = [1,3,4]
print(list1,type(list1))  #[1, 3, 4] <class 'list'>

tup1 = (1,3,4)
print(tup1,type(tup1))  #(1, 3, 4) <class 'tuple'>

set1 = {1,3,4}
print(set1,type(set1))  #{1, 3, 4} <class 'set'>


dict1 = {"name":"zhangsan","age":20}
print(dict1,type(dict1))  #{'name': 'zhangsan', 'age': 20} <class 'dict'>

print("早上好")
print("中午好")
print("下午好")

score=95
if score >= 90:
    print("优秀")
elif score>80:
    print("良好")
elif score>60:
    print("一般")
else:
    print("不及格")