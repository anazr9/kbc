from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import secondfff
def rules():
    root = Tk() 
    root.geometry("1366x768")
    root.configure(bg="#324AEE")
    root.resizable(0,0)
    frame=Frame(root,bg="#324AEE",height=768,width=1366)
    frame.place(x=0,y=0)
    img2 = Image.open("polygon1.png") 
    img2 = img2.resize((1200, 600), Image.ANTIALIAS) 
    img2 = ImageTk.PhotoImage(img2)
    img = Image.open("polygon1.png") 
    img = img.resize((405, 370), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img)
    img1 = Image.open("polygonyellow1.png") 
    img1 = img1.resize((405, 370), Image.ANTIALIAS) 
    img1 = ImageTk.PhotoImage(img1)
    c=Canvas(frame,bg='#324AEE',width=1366,height=150,highlightthickness=0)
    c.place(x=0,y=10)
    c.create_image(650, 65, anchor=CENTER, image=img2)
    reg=Label(frame,text='Fastest Finger First Rules',bg="#0A22B1",fg="white",font="Courier 30 bold")
    reg.place(x=280,y=55)
    def on_enter1(e):
        btn['image'] = img1
    def on_leave1(e):
        btn['image'] = img
    def prr():
            root.destroy()
            secondfff.fff()
    btn=Button(frame,text='Start',height=100,width=400,command=prr,font="Courier 17 bold",activebackground='#324AEE',
                     bg="#324AEE",fg="white",image=img,compound="center",relief="groove",bd=0)
    btn.place(x=750,y=600)
    fff=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 17 bold",text='1. You will be given 20 seconds for the question')
    fff.place(x=10,y=200)
    fff1=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 17 bold",text='2. After 5 seconds the options will be appear')
    fff1.place(x=10,y=300) 
    fff2=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 17 bold",text='3. You have to select the options in the correct sequence')
    fff2.place(x=10,y=400)
    fff3=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 17 bold",text='4. The fastest to select all the right options will sit on the hot seat')
    fff3.place(x=10,y=500)
    btn.bind("<Enter>", on_enter1)
    btn.bind("<Leave>", on_leave1)

    root.mainloop()
