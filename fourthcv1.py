from tkinter import *
from PIL import ImageTk,Image
from datetime import date
import mysql.connector
import leaderboard
def cheque(prize):
    prize=prize
    db=mysql.connector.connect(user="root",password="root",host="localhost",database='kbc')
    cursor=db.cursor()
    cursor.execute('select fname,lname from registration ORDER BY id DESC LIMIT 1;')
    name=cursor.fetchone()
    from datetime import date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    root = Tk()
    root.geometry('1366x768')
    c = Canvas(root,bg="#324AEE", width=1366, height=768)
    c.place(x=0,y=0)
    img96 = Image.open("cheque.jpg") 
    img96 = img96.resize((1200, 500), Image.ANTIALIAS) 
    img96 = ImageTk.PhotoImage(img96)
    c.create_image(700, 350, anchor=CENTER, image=img96)
    lbl=Label(c,text='₹',font='Courier 35 ',bg='white')
    lbl.place(x=970,y=280)
    lblprize=Label(c,text=prize,font='Courier 23 ',bg='white',anchor='w')
    lblprize.place(x=1015,y=290)
    lblname=Label(c,text=name[0]+' '+name[1],font='Vijaya 23 ',bg='white',anchor='w')
    lblname.place(x=270,y=279)
    if prize=='10,000':
        lblal=Label(c,text='ten thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)
    elif prize=='20,000':
        lblal=Label(c,text='twenty thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='40,000':
        lblal=Label(c,text='fourty thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='80,000':
        lblal=Label(c,text='eighty thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='1,60,000':
        lblal=Label(c,text='one lakh sixty thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='3,20,000':
        lblal=Label(c,text='three lakh twenty thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='6,40,000':
        lblal=Label(c,text='six lakh fourty thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='12,50,000':
        lblal=Label(c,text='twelve lakh fifty thousand only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='50,00,000':
        lblal=Label(c,text='fifty lakh only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)        
    elif prize=='1 Crore':
        lblal=Label(c,text='one crore only/-',font='Vijaya 20',bg='white',anchor='w')
        lblal.place(x=200,y=340)       
    date=Label(c,text=d1,font='Courier 20',bg='white')
    date.place(x=1030,y=200)
    sign=Image.open('signature.png')
    sign=sign.resize((200, 150), Image.ANTIALIAS)
    sign=ImageTk.PhotoImage(sign)
    c.create_image(1000, 450, anchor=CENTER, image=sign)
    rupeelbl=Label(c,text='Rupees',font='times 13 bold',bg='white',anchor='w')
    rupeelbl.place(x=1145,y=370)
    btn=Button(c)
    root.update()
    root.after(5000)
    root.mainloop()
