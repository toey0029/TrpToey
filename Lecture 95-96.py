from tkinter import *

def sayHelloWorld():
    print("Hello World")
MainWindow = Tk()
MainWindow.title("Hello Wondow")
button = Button(MainWindow,text = "Click1",command = sayHelloWorld).grid(row = 2,column = 1)
button1 = Button(MainWindow,text = "Click2",command = sayHelloWorld).grid(row = 1,column = 1)
button2 = Button(MainWindow,text = "Click3",command = sayHelloWorld).grid(row = 0,column = 2)
label = Label(MainWindow,text = "Hello",width = 20,fg = "red",bg = "blue").grid(row=0,column=1)
MainWindow.mainloop()