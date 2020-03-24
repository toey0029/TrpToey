def login():
    username = input("Username : ")
    password = input("password : ")
    while username != ("toey") or password != ("1234"):
        if True:
            print("Login Fail...")
            login()
    else:
        print("Wellcome Toey")
        showMenu()
def showMenu():
    print("---ishop---")
    print("1.Vat Caculator")
    print("2.Price Calculator")
login()