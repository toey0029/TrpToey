systemMenu = {"ข้าวมันไก่":40,"ข้าวผัด":45,"ข้าวไข่เจียว":30,"ข้าวหมูทอด":40}
menuList = []
def showBill():
    print("---My Food---")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    print(totalPrice)

while True:
    menuName = input("Enter your menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()