brands = ['er', 'ma', 'de', '34', 'ty', "e"]
i = 0
while i < len(brands):
    if 'e' in brands[i] or '3' in brands[i]:
        del brands[i]
        continue
    i += 1
print(brands)
