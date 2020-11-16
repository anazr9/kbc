from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import testthirdgame
root = Tk() 
root.geometry("1366x768")
root.configure(bg="#324AEE")
root.resizable(0,0)
frame=Frame(root,bg="#324AEE",height=768,width=1366)
frame.place(x=0,y=0)
img2 = Image.open("polygon1.png") 
img2 = img2.resize((900, 600), Image.ANTIALIAS) 
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
reg=Label(frame,text='Game Rules',bg="#0A22B1",fg="white",font="Courier 30 bold")
reg.place(x=500,y=55)
def on_enter1(e):
    btn['image'] = img1
def on_leave1(e):
    btn['image'] = img
def prr():
    root.destroy()
    testthirdgame.game()
btn=Button(frame,text='Start',height=100,width=400,command=prr,font="Courier 17 bold",activebackground='#324AEE',
                 bg="#324AEE",fg="white",image=img,compound="center",relief="groove",bd=0)
btn.place(x=750,y=600)
fff=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 13 bold",text='1. There will be 11 questions')
fff.place(x=10,y=200)
fff1=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 13 bold",text='2. They are arranged by increasing order of difficulty')
fff1.place(x=10,y=250) 
fff2=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 13 bold",text='3. Simplier questions first and are worth less')
fff2.place(x=10,y=300)
fff3=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 13 bold",text='4. Answering the hardest 11th question, will make you a winner of ₹1 Crore!')
fff3.place(x=10,y=350)
fff3=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 13 bold",text='5. There are no lifelines!!')
fff3.place(x=10,y=400)
fff3=Label(frame,bg='#324AEE',bd=0,fg="white",font="Courier 13 bold",text='6. Wrong answer will not make you lose any money so be chilled and relax')
fff3.place(x=10,y=450)
btn.bind("<Enter>", on_enter1)
btn.bind("<Leave>", on_leave1)

root.mainloop()
