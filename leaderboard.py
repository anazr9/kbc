from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
def leader():
    db=mysql.connector.connect(user="root",password="root",host="localhost",database='kbc')
    cursor=db.cursor()
    cursor.execute('select * from leaderboard ORDER BY prize DESC LIMIT 4;')
    names=cursor.fetchall()
    prize=''
    print(names)
    root1 = Toplevel() 
    root1.geometry("1366x768")
    root1.configure(bg="#324AEE")
    root1.resizable(0,0)
    frame=Frame(root1,bg="#324AEE",height=768,width=1366)
    frame.place(x=0,y=0)
    img44 = Image.open("polygon1.png") 
    img44 = img44.resize((900, 600), Image.ANTIALIAS) #The (250, 250) is (height, width)
    img44 = ImageTk.PhotoImage(img44)# PIL solution
    c44=Canvas(frame,bg='#324AEE',width=1366,height=150,highlightthickness=0)
    c44.place(x=0,y=10)
    c44.create_image(650, 65, anchor=CENTER, image=img44)
    reg=Label(frame,text='Leaderboard',bg="#0A22B1",fg="white",font="Courier 30 bold")
    reg.place(x=500,y=55)
    l1=Label(frame,bg='#FFD51B',font="Courier 17 bold",text=names[0][0]+' ₹'+str(names[0][1]))
    l1.place(x=10,y=200,width=1366)
    l2=Label(frame,bg='#FFD51B',font="Courier 17 bold",text=names[1][0]+' ₹'+str(names[1][1]))
    l2.place(x=10,y=250,width=1366) 
    l3=Label(frame,bg='#FFD51B',font="Courier 17 bold",text=names[2][0]+' ₹'+str(names[2][1]))
    l3.place(x=10,y=300,width=1366)
    l4=Label(frame,bg='#FFD51B',font="Courier 17 bold",text=names[3][0]+' ₹'+str(names[3][1]))
    l4.place(x=10,y=350,width=1366)
    def cr(lbl,names):
        lbl.config(text=names+' ₹1 Crore')    
    if names[0][1]==10000000:
        cr(l1,names[0][0])
    if names[1][1]==10000000:
        cr(l2,names[1][0])
    if names[2][1]==10000000:
        cr(l3,names[2][0])
    if names[3][1]==10000000:
        cr(l4,names[3][0])        

    root1.mainloop()
    db.commit()
    db.close()
