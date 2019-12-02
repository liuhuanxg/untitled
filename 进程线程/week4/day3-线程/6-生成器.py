def hanshu():
    a=3
    for x in range(10):
        yield x+a
        a+=1

x= hanshu()
for y in x:
    print(y)