from tkinter import *
from tkinter.ttk import *
import tkinter as tkinter
from PIL import ImageTk, Image

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
# def selection():
#    selection = "You selected the option " + str(radio.get())
#    print(selection)
def func(value):
    print(value)
def openNewWindow():

    # Toplevel object which will
    # be treated as a new window
    top = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    top.title("TIET Load Forecasting Tool")

    top.geometry("350x400")
    top.configure(bg='gray25')
    photo = PhotoImage(file = r"G:/Misc/aaa.gif")
    panel = tkinter.Label(top, image = photo , background="gray25")
    panel.pack(side = "top", fill = "both", expand = "no")
    # randLab=Label(text=" ",bg="gray25")
    # randLab.pack()
    # A Label widget to show in toplevel
    lab1=tkinter.Label(top,
          text ="Load Forecasting Tool", bg="gray25",fg="white",font=('Courier','14'))
    lab1.pack()
    randLab=tkinter.Label(top,text=" ",bg="gray25")
    randLab.pack()
    radio = IntVar()
    lbl = tkinter.Label(top,text = "Choose Load Forecasting Method:", bg="gray25",fg="white")
    lbl.pack()
    var = StringVar()
    DropDownMenu=tkinter.OptionMenu(top, var, "Random Forest", "Gradient Boosting", command=func,)
    DropDownMenu.config(width=15, bg="gray25")
    DropDownMenu.pack()
    radio = IntVar()
    def selection():
        print(radio.get())
    lb2 = tkinter.Label(top,text = "Is it a special day?", bg="gray25",fg="white")
    lb2.pack()
    R1 = tkinter.Radiobutton(top, text="Normal", bg="gray25",fg="white", variable=radio, value=0,
                      command=selection)
    R1.pack( )

    R2 = tkinter.Radiobutton(top, text="Special", bg="gray25",fg="white", variable=radio, value=1,
                      command=selection)
    R2.pack(  )

    lb3 = tkinter.Label(top,text = "Enter Average Monthly Temperature:", bg="gray25",fg="white")
    lb3.pack()
    entry1 = tkinter.Entry(top,bg="gray25", text="Username:",fg="white")
    entry1.pack()
    label = tkinter.Label(top,bg="gray25")
    label.pack()

master.title("TIET Load Forecasting Tool")

master.geometry("350x400")
master.configure(bg='gray25')




# a button widget which will open a
# new window on button click
# btn = Button(master,
#              text ="Click to open a new window",
#              command = openNewWindow)

photo = PhotoImage(file = r"G:/Misc/aaa.gif")
panel = tkinter.Label(master, image = photo , background="gray25")
panel.pack(side = "top", fill = "both", expand = "no")
Label(master,text=" kghg",background='gray25',foreground='gray25').pack()
Label(master,
              text ="Username",background='gray25',foreground='white').pack()
Entry(master,width='19').pack()
Label(master,text='Password',background='gray25',foreground='white').pack()
Entry(master,width='19',show='*').pack()
Label(master,text=" kghg",background='gray25',foreground='gray25').pack()
Button(master, text="Log In",command=openNewWindow).pack()

# mainloop, runs infinitely
mainloop()
