'''
字典推导式
'''
# a={'a':'b',1:2}
# b={v:k for k,v in a.items()}
# print(b)

# a={k:v for k,v in zip('abc','123')}
# print(a)

a={'a':1,'A':3,'b':4,'B':9,'c':10,'d':99}
x=['a','A','B','b','c']
b={k.lower():a.get(k.lower(),0)+a.get(k.upper(),0) for k in a.keys() if k in x}
print(b)