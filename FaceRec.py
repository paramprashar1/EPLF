import face_recognition
import cv2
from PIL import Image
import time
from functools import partial

globX=-1

cam = cv2.VideoCapture(0)
s, img = cam.read()
if s:


    face_1_image = face_recognition.load_image_file("F:/Placement docs/param.jpg")
    face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

    small_frame= cv2.resize(img,(0,0),fx=0.25,fy=0.25)

    rgb_small_frame = small_frame[:,:,::-1]

    face_locations= face_recognition.face_locations(rgb_small_frame)
    face_encodings= face_recognition.face_encodings(rgb_small_frame,face_locations)

    check=face_recognition.compare_faces(face_1_face_encoding,face_encodings)

    top,right,bottom,left=(face_recognition.face_locations(img))[0]

    print("found face at top:{}, left:{}, bottom:{}, right:{}".format(top,left,bottom,right))
    face_image=img[top:bottom,left:right]
    pil_image=Image.fromarray(face_image)
    pil_image.save("face.jpg")

    print(check)
    if check[0]:
        print("Welcome Param!")
        key=1;
    else:
        print("unauthorized access")
        key=0;
o=0;
if key == o:
        from tkinter import *
        from tkinter.ttk import *
        import tkinter as tkinter
        from PIL import ImageTk, Image

        master = Tk()


        master.geometry("200x200")




            # print(a)
        # def validateLogin(username, password):
	    #     print("username entered :", username.get())
	    #     print("password entered :", password.get())
	    #     return


            # be=Toplevel(master)
            # be.title("TIET LOAD FORECASTING TOOL")
            # be.geometry("350x400")
            # be.configure(bg='gray25')
        #
        #     frame = Frame(be)
        #     frame.configure(width=50, height=50)
        #     frame.pack()
        #     Label(be,text="422906.7131999",anchor='center').pack()
        def openNewWindow():

            def func(value):
                if(value=='Random Forest'):
                    globX=0
                else:
                    globX=1
                # print(globX)
                # print(aselection())
            def lastwin():
                weath=int(entry1.get())
                mnt=int(entry2.get())
                # print(aselection())
                variab8=[]
                variab8.append(mnt)
                variab8.append(weath)
                variab8.append(aselection())
                print(variab8)
                Xnew2=[variab8]
                # print(variab81)
                import joblib
                if(globX==0):
                    loaded_model = joblib.load('randomF.sav')
                else:
                    loaded_model = joblib.load('gradb.sav')
                # # result = loaded_model.score(X_test, Y_test)
                # Xnew2=[[454,63,0]]
                #
                predc=10**loaded_model.predict(Xnew2)
                print(predc)
                my_string_var = StringVar()
                my_string_var.set(str(predc))
                labeld = tkinter.Label(top,textvariable = my_string_var,bg="gray25",fg="white",font=('Courier','21'))
                labeld.pack()
                labeld.place(relx=1.0, rely=1.0, anchor='se')
            top = Toplevel(master)


            top.title("TIET Load Forecasting Tool")

            top.geometry("350x400")
            top.configure(bg='gray25')
            photo = PhotoImage(file = r"G:/Misc/aaa.gif")
            panel = tkinter.Label(top, image = photo , background="gray25")
            panel.pack(side = "top", fill = "both", expand = "no")

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
            def aselection():
                return radio.get()
            lb2 = tkinter.Label(top,text = "Is it a special month?", bg="gray25",fg="white")
            lb2.pack()
            R1 = tkinter.Radiobutton(top, text="Normal", bg="gray25",fg="white", variable=radio, value=0,
                              command=aselection)
            R1.pack( )

            R2 = tkinter.Radiobutton(top, text="Special", bg="gray25",fg="white", variable=radio, value=1,
                              command=aselection)
            R2.pack(  )

            lb3 = tkinter.Label(top,text = "Enter Average Monthly Temperature:", bg="gray25",fg="white")
            lb3.pack()
            entry1 = tkinter.Entry(top,bg="gray25", text="Temp:",fg="white")
            entry1.pack()
            lb4 = tkinter.Label(top,text = "Enter Month number:", bg="gray25",fg="white")
            lb4.pack()
            entry2 = tkinter.Entry(top,bg="gray25", text="mth:",fg="white")
            entry2.pack()
            label = tkinter.Label(top,bg="gray25")
            btn = tkinter.Button(top,text='Calculate',background='gray25',foreground='white',command=lastwin)

            label.pack()
            btn.pack()

        master.title("TIET Load Forecasting Tool")

        master.geometry("350x400")
        master.configure(bg='gray25')




        # def newwin:

        def checko():
            usn=ss.get()
            psw=ls.get()
            print(type(usn))
            print(psw)
            if((usn=='param.prashar24@gmail.com') and (psw=='01234')):
                openNewWindow()
            else:
                tlbl=tkinter.Label(master,text='Please try again',background='gray25',foreground='white')
                tlbl.pack()

        photo = PhotoImage(file = r"G:/Misc/aaa.gif")
        panel = tkinter.Label(master, image = photo , background="gray25")
        panel.pack(side = "top", fill = "both", expand = "no")
        # Label(master,text=" kghg",background='gray25',foreground='gray25').pack()
        us=tkinter.Label(master,
                      text ="Username",background='gray25',foreground='white')
        us.pack()
        ss=tkinter.Entry(master,width='19')
        ss.pack()
        bs=tkinter.Label(master,text='Password',background='gray25',foreground='white')
        bs.pack()
        ls=Entry(master,width='19',show='*')
        ls.pack()
        # def printuser(user,passt):
        #     print(user.get())
        #     print(passt.get())

        # Label(master,text=" kghg",background='gray25',foreground='gray25').pack()
        bn=tkinter.Button(master, text="Log In",command=checko)
        bn.pack()

        mainloop()


if key==1:
        from tkinter import *
        from tkinter.ttk import *
        import tkinter as tkinter
        from PIL import ImageTk, Image

        top = Tk()


        top.title("TIET Load Forecasting Tool")
        def lastwin():


            weath=int(entry1.get())
            mnt=int(entry2.get())
            print(selection())
            variab8=[]
            variab8.append(mnt)
            variab8.append(weath)
            variab8.append(selection())
            Xnew2=[variab8]
            # print(variab81)
            import joblib
            if(globX==0):
                loaded_model = joblib.load('randomF.sav')
            else:
                loaded_model = joblib.load('gradb.sav')
            # # result = loaded_model.score(X_test, Y_test)
            # Xnew2=[[454,63,0]]
            #
            predc=10**loaded_model.predict(Xnew2)
            print(predc)
            # labeld=tkinter.Label(top,text="0",bg="gray25")
            # labeld.pack()

            my_string_var = StringVar()
            my_string_var.set(str(predc))

            labeld = tkinter.Label(top,textvariable = my_string_var,bg="gray25",fg="white",font=('Courier','21'))
            labeld.pack()
            labeld.place(relx=1.0, rely=1.0, anchor='se')
            # time.sleep(10)
            # labeld.destroy()
            # be=Toplevel(top)
            # # be.title("TIET LOAD FORECASTING TOOL")
            # # be.geometry("350x400")
            # # be.configure(bg='gray25')
            #
            # frame = Frame(be)
            # frame.configure(width=50, height=50)
            # frame.pack()
            # Label(be,text="4554548",anchor='center').pack()
        def func(value):
            if(value=='Random Forest'):
                globX=0
            else:
                globX=1
            print(globX)
        top.geometry("350x400")
        top.configure(bg='gray25')
        top.resizable(False, False)
        photo = PhotoImage(file = r"G:/Misc/aaa.gif")
        panel = tkinter.Label(top, image = photo , background="gray25")
        panel.pack(side = "top", fill = "both", expand = "no")

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
            # print(radio.get())
            return radio.get()

        lb2 = tkinter.Label(top,text = "Is it a special month?", bg="gray25",fg="white")
        lb2.pack()
        R1 = tkinter.Radiobutton(top, text="Normal", bg="gray25",fg="white", variable=radio, value=0,
                          command=selection)
        R1.pack( )

        R2 = tkinter.Radiobutton(top, text="Special", bg="gray25",fg="white", variable=radio, value=1,
                          command=selection)
        R2.pack(  )

        lb3 = tkinter.Label(top,text = "Enter Average Monthly Temperature:", bg="gray25",fg="white")
        lb3.pack()
        entry1 = tkinter.Entry(top,bg="gray25", text="Temp",fg="white")
        entry1.pack()
        lb4 = tkinter.Label(top,text = "Enter Monthly number:", bg="gray25",fg="white")
        lb4.pack()
        entry2 = tkinter.Entry(top,bg="gray25", text="Month",fg="white")
        entry2.pack()
        label = tkinter.Label(top,bg="gray25")
        label.pack()


        btn = tkinter.Button(top,text='Calculate',background='gray25',foreground='white',command=lastwin)
        btn.pack()

        mainloop()
