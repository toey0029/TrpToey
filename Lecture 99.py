from tkinter import *
import math

def leftClickbutton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))

mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง (Cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="คำนวณ")
calculateButton.bind("<Button-1>",leftClickbutton)
calculateButton.grid(row=2,column=0)
labelResult = Label(mainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
mainWindow.mainloop()