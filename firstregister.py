from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from datetime import date
import socket
import fffrules
root = Tk() 
root.geometry("1366x768")
root.configure(bg="#324AEE")
root.resizable(0,0)
frame2=Frame(root,bg="#324AEE",height=768,width=1366)
frame2.place(x=0,y=0)
frame=Frame(frame2,bg="#324AEE",height=300,width=680)
frame.place(x=300,y=200)
frame1=Frame(frame2,bg="#324AEE",height=200,width=900)
frame1.place(x=200,y=0)
img2 = Image.open("polygon1.png") 
img2 = img2.resize((900, 600), Image.ANTIALIAS) 
img2 = ImageTk.PhotoImage(img2)
img = Image.open("polygon1.png") 
img = img.resize((405, 370), Image.ANTIALIAS) 
img = ImageTk.PhotoImage(img)
img1 = Image.open("polygonyellow1.png") 
img1 = img1.resize((405, 370), Image.ANTIALIAS) 
img1 = ImageTk.PhotoImage(img1)
def on_enter1(e):
    btn['image'] = img1
def on_leave1(e):
    btn['image'] = img
c=Canvas(frame2,bg='#324AEE',width=1366,height=150,highlightthickness=0)
c.place(x=0,y=42)
c.create_image(600, 65, anchor=CENTER, image=img2)
reg=Label(frame2,text='KBC Registration Form',bg="#0A22B1",fg="white",font="Courier 30 bold")
reg.place(x=300,y=90)
def prr():
    i=0
    db=mysql.connector.connect(user="root",password="root",host="localhost",database='kbc')
    cursor=db.cursor()
    fname1=fname.get()
    if(re.match('[a-zA-Z]',fname1)):
        vfname.config(text='')
        i=i+1
    else:
        vfname.config(text='Enter proper name')    
    lname1=lname.get()
    if(re.match('[a-zA-Z]',lname1)):
        vlname.config(text='')
        i=i+1
    else:
        vlname.config(text='Enter proper name')
    age1=age.get()
    if (re.match('[0-9]',age1)):
        vage.config(text='')
        i=i+1
    else:
        vage.config(text='Enter proper age')
    job1=job.get()
    if re.match('[a-zA-Z]',job1):
        vjob.config(text='')
        i=i+1
    else:
        vjob.config(text='Enter proper job')
    city1=city.get()
    if re.match('[a-zA-Z]',city1):
        vcity.config(text='')
        i=i+1
    else:
        vcity.config(text='Enter proper City')
    mob1=mob.get()
    if re.match('[0-9]',mob1) and len(mob1)==10:
        vmob.config(text='')
        i=i+1
    else:
        vmob.config(text='Enter proper mobile number')
    email1=email.get()
    if re.match("\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",email1):
        vemail.config(text='')
        i=i+1
    else:
        vemail.config(text='Enter proper email')
    if i==7:
        cursor.execute('insert into registration(fname,lname,age,job,city,mobile,email)values(%s,%s,%s,%s,%s,%s,%s)',(fname1,lname1,age1,job1,city1,mob1,email1))
        db.commit()
        db.close()
        root.destroy()
        fffrules.rules()

        
        
        
lblfname=Label(frame,text='First name',fg="white",font="Courier 17 bold",bg="#324AEE")
lblfname.grid(row=0,column=0)
fname=Entry(frame,font="Courier 17 bold")
fname.grid(row=0,column=1)
vfname=Label(frame,fg="#FFD51B",font="Courier 17 bold",bg="#324AEE")
vfname.grid(row=0,column=2)


lbllname=Label(frame,text='Last name',fg="white",font="Courier 17 bold",bg="#324AEE")
lbllname.grid(row=1,column=0)
lname=Entry(frame,font="Courier 17 bold")
lname.grid(row=1,column=1)
vlname=Label(frame,fg="#FFD51B",font="Courier 17 bold",bg="#324AEE")
vlname.grid(row=1,column=2)


lblage=Label(frame,text='Age',fg="white",font="Courier 17 bold",bg="#324AEE")
lblage.grid(row=2,column=0)
age=Entry(frame,font="Courier 17 bold")
age.grid(row=2,column=1)
vage=Label(frame,fg="#FFD51B",font="Courier 17 bold",bg="#324AEE")
vage.grid(row=2,column=2)


lbljob=Label(frame,text='Job',fg="white",font="Courier 17 bold",bg="#324AEE")
lbljob.grid(row=3,column=0)
job=Entry(frame,font="Courier 17 bold")
job.grid(row=3,column=1)
vjob=Label(frame,fg="#FFD51B",font="Courier 17 bold",bg="#324AEE")
vjob.grid(row=3,column=2)

lblcity=Label(frame,text='City',fg="white",font="Courier 17 bold",bg="#324AEE")
lblcity.grid(row=4,column=0)
city=Entry(frame,font="Courier 17 bold")
city.grid(row=4,column=1)
vcity=Label(frame,fg="#FFD51B",font="Courier 17 bold",bg="#324AEE")
vcity.grid(row=4,column=2)


lblmob=Label(frame,text='Mobile Number',fg="white",font="Courier 17 bold",bg="#324AEE")
lblmob.grid(row=5,column=0)
mob=Entry(frame,font="Courier 17 bold")
mob.grid(row=5,column=1)
vmob=Label(frame,fg="#FFD51B",font="Courier 17 bold",bg="#324AEE")
vmob.grid(row=5,column=2)

lblemail=Label(frame,text='Email Address',fg="white",font="Courier 17 bold",bg="#324AEE")
lblemail.grid(row=6,column=0)
email=Entry(frame,font="Courier 17 bold")
email.grid(row=6,column=1)
vemail=Label(frame,fg="#FFD51B",font="Courier 17 bold",bg="#324AEE")
vemail.grid(row=6,column=2)


btn=Button(frame2,text='Submit',height=100,width=400,command=prr,font="Courier 17 bold",activebackground='#324AEE',
                 bg="#324AEE",fg="white",image=img,compound="center",relief="groove",bd=0)
btn.place(x=400,y=460)
btn.bind("<Enter>", on_enter1)
btn.bind("<Leave>", on_leave1)

root.mainloop()
