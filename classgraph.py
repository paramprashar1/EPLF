class Name:
    def __init__(self):
        self.myname = "harry"

    def printaname(self):
        print "Name", self.myname

    def main(self):
        self.printaname()

if __name__ == "__main__":
    objName = Name()
    objName.main()
    import tkinter as tk
    from tkinter import ttk

    # Creating tkinter window

    window = tk.Tk()
    window.title('Load Forecasting')
    window.configure(bg='gray25')
    window.geometry('350x400')

    # label text for title
    ttk.Label(window, text = "    Welcome User!    ",
              background = 'gray25', foreground ="white",
              font = ("Times New Roman", 12)).grid(row = 0, column = 0)

    # label
    ttk.Label(window, text = "Select the Method :",
              font = ("Times New Roman", 10)).grid(column = 0,
              row = 5, padx = 10, pady = 25)

    # Combobox creation
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(window, width = 14, textvariable = n,)

    # Adding combobox drop down list
    monthchoosen['values'] = ('Random Forest','Gradient Boost')

    monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    ttk.Label(window, text = "Enter Temperature:",
              font = ("Times New Roman", 10)).grid(column = 0,
              row = 10, padx = 10, pady = 25)
    ttk.Entry(window, width=10).grid(column = 1,
    row = 10, padx = 10, pady = 25)


    ttk.Label(window, text = "Is it a special month:",
              font = ("Times New Roman", 10)).grid(column = 0,
              row = 15, padx = 10, pady = 25)

    SplMonth =tk.StringVar()


    ttk.Radiobutton(window, text='Special',value='1',variable=SplMonth,command=selected).grid(column = 1,
    row = 15, padx = 10, pady = 25)

    ttk.Radiobutton(window, text='Normal',value='0',variable=SplMonth,command=selected).grid(column = 1,
    row = 16, padx = 10)
    def selected(self):
        if self.SplMonth.get()==1:
            splvar=1
        elif self.SplMonth.get()==0:
            splvar=0
        else:
            "do something"
    ttk.Button(window,text='Go').grid(column = 1,
    row = 17, padx = 10,pady=10)

    #add command to Button

    window.mainloop()
    print(splvar)
