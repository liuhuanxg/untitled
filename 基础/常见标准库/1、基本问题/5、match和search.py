import re
print(re.match("func","function"))
print(re.match("func","function").span())
print(re.match("func1","function"))

print(re.search("tion","funtion"))
print(re.search("tion","funtion").span())
print(re.search("tion1","function"))