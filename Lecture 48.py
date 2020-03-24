number = int(input(">>"))
text = " "
for a in range(number):
    text = text + "*"
    print(text)

number = int(input(">>"))
for x in range(number):
    text = ""
    for y in range(x+1):
        text += "*"
    print(text)

number = int(input(">>"))
for x in range(number):
    print("*"*(x+1))