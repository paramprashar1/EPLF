import tkinter as tkinter
from tkinter import *
# from PIL import ImageTk, Image
from tkinter.ttk import *
from tkinter import ttk


window = tkinter.Tk()
window.geometry("350x400")
window.configure(bg='gray25')
window.title("Load Forecasting")

lbl0 = tkinter.Label(window, text=" ", font=("new roman", 20), bg="gray25",fg="white")
lblx= tkinter.Label(window, text=" ", font=("new roman", 20), bg="gray25")

lbl1 = tkinter.Label(window, text="Welcome User!:", font=("new roman", 8), bg="gray25",fg="white")
lbl2 = tkinter.Label(window, text="Choose Load Forecasting method:", font=("new roman", 11), bg="gray25",fg="white")




variable = StringVar(window)
variable.set("") # default value
w = OptionMenu(window, variable, "Gradient Boost", "Random Forest")

Nweek= tkinter.Label(window, text="Enter month", font=("new roman", 11), bg="gray25",fg="white")
entryO = tkinter.Entry(window,bg="gray25")

Ntemp = tkinter.Label(window, text="Enter Average Temperature in ºC:", font=("new roman", 11), bg="gray25",fg="white")
entryT = tkinter.Entry(window,bg="gray25")

Nday = tkinter.Label(window, text="Is it a special month:", font=("new roman", 11), bg="gray25",fg="white")

print(variable.get())



n = StringVar(window)
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()

lblx.pack()
lbl1.pack()
lbl2.pack()
# lbl0.pack()
w.pack()
Nweek.pack()
entryO.pack()
Ntemp.pack()
entryT.pack()
Nday.pack()
lbl0.pack()

window.mainloop()
