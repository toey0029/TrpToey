user = input("ID : ")
password = input("password : ")
if user == "Toey" and password == "1234":
    print("wellcome")
    print("---ishop---")
    print("1.Vat Caculator")
    print("2.Price Calculator")
    user = int(input(">>"))
    if user == 1:
        price = int(input("Price : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif user == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product : "))
        print(price1+price2)
else:
    print("Login Fail")
