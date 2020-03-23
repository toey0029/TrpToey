corrrectNumber = 17
userGuess = 0
while userGuess != corrrectNumber:
    userGuess = int(input("please guess a number : "))
    if userGuess > corrrectNumber:
        print("Too Large")
    elif userGuess < corrrectNumber:
        print("Too small")
    elif userGuess == corrrectNumber:
        print("Correct !!")