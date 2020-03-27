menuList = []

def showBill():
    print("---My Food---")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number])
        totalPrice += int(menuList[number][1])
    print(totalPrice)

while True:
    menuName = input("Enter your menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])
showBill()
#print(menuList)

