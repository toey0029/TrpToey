words = {"Bird":"นก","Ant":"มด","Cat":"แมว","Milk":"นม","Dog":"สุนัข"}
print(words["Bird"])
print(words.items())
print(type(words.keys()))
print(type(words.values()))
print(words.keys())
for a in words.keys():
    print(a)
words.clear()