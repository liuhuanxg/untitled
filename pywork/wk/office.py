import random
teachers=['a','b','c','d','e','f','g','h']
office=[[],[],[]]
for i in range(len(teachers)):
    random.choice(office).append(teachers[i])
print(office)