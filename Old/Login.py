import tkinter as tkinter
from tkinter import *
# from PIL import ImageTk, Image
from tkinter.ttk import *

window = tkinter.Tk()
window.geometry("350x400")
window.configure(bg='gray25')
window.title("Load Forecasting")
# # img = ImageTk.PhotoImage(Image.open("C:/Users/Param Prashar/Desktop/aaa.gif"))
# panel = Label(root, image = img,bg="gray25")
# panel.pack(side = "top", fill = "both", expand = "yes")

photo = PhotoImage(file = r"G:/Misc/aaa.gif")
panel = Label(window, image = photo , background="gray25")
panel.pack(side = "top", fill = "both", expand = "yes")

lbl0 = tkinter.Label(window, text=" ", font=("new roman", 20), bg="gray25",fg="white")
lblx= tkinter.Label(window, text="", font=("new roman", 20), bg="gray25")
lbly= tkinter.Label(window, text="", font=("new roman", 20), bg="gray25")
lblz= tkinter.Label(window, text="", font=("new roman", 20), bg="gray25")
lbla= tkinter.Label(window, text="", font=("new roman", 20), bg="gray25")

lbl1 = tkinter.Label(window, text="Username:", font=("new roman", 15), bg="gray25",fg="white")
entry1 = tkinter.Entry(window,bg="gray25", text="Username:",fg="white")


lbl2 = tkinter.Label(window, text="Password:", font=("new roman", 15), bg="gray25",fg="white")
entry2 = tkinter.Entry(window,bg="gray25")

btn = tkinter.Button(window, text="Log In",fg="white",bg="gray25")
# lblas = tkinter.Label(window, text="Forgot Password?", font=("new roman", 15), bg="gray25",fg="thistle4", underline=0)
# lbl3 = tkinter.Label(window, text="Alternative Method(s)", font=("new roman", 10), bg="gray25",fg="thistle4")
# btnx = tkinter.Button(window, text="Scan your face",fg="white",bg="gray25")



lblx.pack()
lbl1.pack()
entry1.pack()

lbl2.pack()
entry2.pack()
lblz.pack()
btn.pack()



lbly.pack()
# lblas.pack()
# lbl3.pack()
lbla.pack()

# btnx.pack()
lbl0.pack()

window.mainloop()
