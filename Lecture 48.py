#number = int(input(">>"))
#text = ""
#for a in range(number):
    #text = text + "*"
    #print(text)

number = int(input(">>"))
for x in range(3):
    text = ""
    for y in range(x+1):
        text += "*"
    print(text)

number = int(input(">>"))
for x in range(3):
    print("*"*(x+1))