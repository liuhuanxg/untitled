brands=['er','ma','de','34','ty']
l=len(brands)
i=0
while i<l:
    if 'e' in brands[i] or '3' in brands[i]:
        del brands[i]
        l-=1
    i+=1
print(brands)