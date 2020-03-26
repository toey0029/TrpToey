menuList = []
priceList = []
def showBill():
    print("My Food")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
while True:
    menuName = input("Enter your menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
#def total():

showBill()

