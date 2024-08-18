# readline一行一行的读取，然后手动存储在列表中

# readlines读取整个文档，然后存储在一个列表中，包括换行符

list = []
with open('a.txt', 'r') as fp:
    data = fp.readline()
    print(data)
    list.append(data)
    while data != '':
        data = fp.readline()
        list.append(data)

print(list)  # ['asfdasfasfas\n', 'asfasfas', '']

with open('a.txt', 'r') as fp:
    data = fp.readlines()
print(data)
