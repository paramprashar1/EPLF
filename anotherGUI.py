from tkinter import *

def selection():
   selection = "You selected the option " + str(radio.get())
   label.config(text = selection)
def func(value):
    print(value)


top = Tk()
top.geometry("350x400")
top.configure(bg='gray25')
top.title("TIET Load Forecasting Tool ")
photo = PhotoImage(file = r"G:/Misc/aaa.gif")
panel = Label(top, image = photo , background="gray25")
panel.pack(side = "top", fill = "both", expand = "no")
randLab=Label(text=" ",bg="gray25")
randLab.pack()
radio = IntVar()
lbl = Label(text = "Choose Load Forecasting Method:", bg="gray25",fg="white")
lbl.pack()
var = StringVar()
DropDownMenu=OptionMenu(top, var, "Random Forest", "Gradient Boosting", command=func,)
DropDownMenu.config(width=15, bg="gray25")
DropDownMenu.pack()
radio = IntVar()
lb2 = Label(text = "Is it a special day?", bg="gray25",fg="white")
lb2.pack()

R1 = Radiobutton(top, text="Normal", bg="gray25",fg="white", variable=radio, value=0,
                  command=selection)
R1.pack( )

R2 = Radiobutton(top, text="Special", bg="gray25",fg="white", variable=radio, value=1,
                  command=selection)
R2.pack(  )

lb3 = Label(text = "Enter Average Monthly Temperature:", bg="gray25",fg="white")
lb3.pack()
entry1 = Entry(top,bg="gray25", text="Username:",fg="white")
entry1.pack()



label = Label(top)
label.pack()
top.mainloop()
