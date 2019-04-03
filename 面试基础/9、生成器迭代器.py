#生成器、减小占用的内存，随取随用

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
    # return 'done'
        yield a
s= fib(10)
for i in s:
    print(i)

a=['a,1','bb,3,22','c,3,4','b,5']
b=['a,2','nn,1','d,2','a,3']


