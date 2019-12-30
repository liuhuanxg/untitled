dict={}
str1="{k1:v1,k2:v2,k3,k4:v4,v5,k6:v7}"
a=str1[1:-1].split(',')
for x in a:
    if x.isalnum():
        continue
    y=x.split(':')
    dict[y[0]]=y[1]
print(dict)