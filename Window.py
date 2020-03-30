from tkinter import *

root = Tk()
root.option_add("*Font", "Calibri 25")
Label(root, text = "apple").pack(anchor = E)
Label(root, text = "apple",bg = "blue").pack(fill = X,anchor = W)
Label(root, text = "apple",bg = "yellow",width = 15).pack()
Label(root, text = "apple",fg = "red",bg = "green").pack()
Label(root, text = "green\ntea",fg = "red",bg = "green").pack(fill = X)
Label(root, text = "Haaaaaaaaaaassssssssswwwwwwwwweeeegggggggggggdddddddgggggggg",fg = "red",bg = "green",wraplength=400).pack()
root.mainloop()