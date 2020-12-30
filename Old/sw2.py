import tkinter as tkinter

window = tkinter.Tk()
window.geometry("350x400")

window.title("Load Forecasting")
lbl0 = tkinter.Label(window, text="LOAD FORECASTING", font=("new roman", 20))
lblx= tkinter.Label(window, text="", font=("new roman", 20))
lbly= tkinter.Label(window, text="", font=("new roman", 20))

lbl1 = tkinter.Label(window, text="Month", font=("new roman", 15))
entry1 = tkinter.Entry(window)


lbl2 = tkinter.Label(window, text="Year:", font=("new roman", 15))
entry2 = tkinter.Entry(window)

btn = tkinter.Button(window, text="Calculate")


lbl0.pack()

lblx.pack()
lbl1.pack()
entry1.pack()

lbl2.pack()
entry2.pack()

btn.pack()






window.mainloop()