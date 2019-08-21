str1="k:1|j:2"
list1=str1.split("|")
for i in list1:
    print((i.split(":"),))
    for k,v in (i.split(":"),):
        print(k,v)

for k,v in (["k","1"],):
    print(k,v)