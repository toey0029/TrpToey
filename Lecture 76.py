#fruits = {"apple","banana","orange","pineapple"}
#print(fruits)
#fruits.remove("banana")
#print(fruits)
#fruits.add("grape")
#del fruits
userInput = int(input("Enter Number of Your Favorite Fruits : "))
myFruits = set()
while(len(myFruits)<userInput):
    myFruits.add(input("Fruits : "))
    print(myFruits)