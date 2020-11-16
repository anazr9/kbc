from tkinter import *
from PIL import ImageTk, Image
from time import time, sleep
import mysql.connector
from datetime import date
import fourthcv1
import leaderboard
def game():
    db=mysql.connector.connect(user="root",password="root",host="localhost",database='kbc')
    cursor=db.cursor()
    cursor.execute('select fname from registration ORDER BY id DESC LIMIT 1;')
    name=cursor.fetchone()
    root = Tk() 
    root.geometry("1366x768")
    root.configure(bg="#324AEE")
    root.resizable(0,0)
    img = Image.open("polygon1.png") 
    img = img.resize((405, 370), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img)
    img1 = Image.open("polygonyellow1.png") 
    img1 = img1.resize((405, 370), Image.ANTIALIAS) 
    img1 = ImageTk.PhotoImage(img1)
    def on_enter1(e):
        btn1['image'] = img1
    def on_leave1(e):
        btn1['image'] = img
    def on_enter2(e):
        btn2['image'] = img1
    def on_leave2(e):
        btn2['image'] = img
    def on_enter3(e):
        btn3['image'] = img1
    def on_leave3(e):
        btn3['image'] = img
    def on_enter4(e):
        btn4['image'] = img1
    def on_leave4(e):
        btn4['image'] = img
    img2 = Image.open("polygon1.png") 
    img2 = img2.resize((815, 500), Image.ANTIALIAS) 
    img2 = ImageTk.PhotoImage(img2)
    img3=Image.open("polygongreen1.png")
    img3=img3.resize((405,370), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    img4=Image.open("polygonredtransparen.png")
    img4=img4.resize((405,370), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)
    Question1=StringVar()
    Answer1=StringVar()
    Answer2=StringVar()
    Answer3=StringVar()
    Answer4=StringVar()
    Canswer=StringVar()
    btn1 = Button(root ,textvariable=Answer1,height=100,width=400,activebackground='#324AEE',
                 bg="#324AEE",fg="white",font="Courier 15 bold",image=img,compound="center",relief="groove",bd=0)
    btn1.place(x=110,y=560)
    btn1.bind("<Enter>", on_enter1)
    btn1.bind("<Leave>", on_leave1)


    btn2 = Button(root ,textvariable=Answer2,height=100,width=400,activebackground="#324AEE",
                 bg="#324AEE",fg="white",font="Courier 15 bold",image=img,compound="center",relief="groove",bd=0)
    btn2.place(x=515,y=560)
    btn2.bind("<Enter>", on_enter2)
    btn2.bind("<Leave>", on_leave2)

    btn3 = Button(root ,textvariable=Answer3,height=100,width=400,activebackground="#324AEE",
                 bg="#324AEE",fg="white",font="Courier 15 bold",image=img,compound="center",relief="groove",bd=0)
    btn3.place(x=110,y=664)
    btn3.bind("<Enter>", on_enter3)
    btn3.bind("<Leave>", on_leave3)


    btn4 = Button(root ,textvariable=Answer4,height=100,width=400,activebackground="#324AEE",
                 bg="#324AEE",fg="white",font="Courier 15 bold",image=img,compound="center",relief="groove",bd=0)
    btn4.place(x=514,y=664)
    btn4.bind("<Enter>", on_enter4)
    btn4.bind("<Leave>", on_leave4)
    c3=Canvas(root,bg="#0A22B1", width=335, height=768,highlightthickness=1)
    c3.place(x=1028,y=0)
    lbl1=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 1       ₹10,000",width=21,anchor='w')
    lbl1.place(x=20,y=610)
    lbl2=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 2       ₹20,000",width=21,anchor='w')
    lbl2.place(x=20,y=570)
    lbl3=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 3       ₹40,000",width=21,anchor='w')
    lbl3.place(x=20,y=530)
    lbl4=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 4       ₹80,000",width=21,anchor='w')
    lbl4.place(x=20,y=490)
    lbl5=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 5       ₹1,60,000",width=21,anchor='w')
    lbl5.place(x=20,y=450)
    lbl6=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 6       ₹3,20,000",width=21,anchor='w')
    lbl6.place(x=20,y=410)
    lbl7=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 7       ₹6,40,000",width=21,anchor='w')
    lbl7.place(x=20,y=370)
    lbl8=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 8       ₹12,50,000",width=21,anchor='w')
    lbl8.place(x=20,y=330)
    lbl9=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text=  " 9       ₹25,00,000",width=21,anchor='w')
    lbl9.place(x=20,y=290)
    lbl10=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text="10       ₹50,00,000",width=21,anchor='w')
    lbl10.place(x=20,y=250)
    lbl11=Label(c3,bg='#0A22B1',fg="white",font="Courier 15 bold",text="11       ₹1 Crore",width=21,anchor='w')
    lbl11.place(x=20,y=210)
    def rightanswer(btn,prize):
        btn.config(image=img3)        
        rightans=Label(c4,justify="center",bg="#324AEE",bd=0,fg="white",font="Courier 30 bold",text="Right Answer!!!",width=34)        
        rightans.place(x=1,y=60)
        c4.update()
        if prize!='₹1 Crore':
            rightans.after(5000,rightans.destroy())
        else:
            rightans.after(5000)
            lbl11.config(bg="#FFD51B",fg="black",text="11  ◆    ₹1 Crore")
            lbl10.config(bg="#0A22B1",fg="white")
            cursor.execute('select fname from registration ORDER BY id DESC LIMIT 1;')
            name=cursor.fetchone()
            rightans.config(text='!! CROREPATI %s !!' %name)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            btn4.destroy()
            txtQuestion.destroy()
            congrat=Label(c,text=prize,font="Courier 30 bold",width=18,bg='#fed51b',fg='black')
            congrat.place(x=135,y=80)
            c.update()
            congrat.after(5000)
            prize1=10000000
            cursor.execute('insert into leaderboard(name,prize)values (%s,%s)',(name[0],prize1,))
            root.destroy()
            fourthcv1.cheque(prize)

    def wronganswer(btn,prize):
        btn.config(image=img4)
        wrongans=Label(c4,justify="center",bg="#324AEE",bd=0,fg="white",font="Courier 30 bold",text="Wrong Answer!!!",width=34)
        wrongans.place(x=1,y=60)
        c4.update()
        wrongans.after(5000)
        cursor.execute('select fname from registration ORDER BY id DESC LIMIT 1;')
        name=cursor.fetchone()
        if prize=='₹0':
            wrongans.config(text='Better luck next time, %s ☹' %name)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            btn4.destroy()
            txtQuestion.destroy()
            congrat=Label(c,text=prize,font="Courier 30 bold",width=18,bg='#fed51b',fg='black')
            congrat.place(x=135,y=80)
            c.update()
            congrat.after(5000)       

            
        else:
            wrongans.config(text='Congratulations %s You won' %name)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            btn4.destroy()
            txtQuestion.destroy()
            congrat=Label(c,text=prize,font="Courier 30 bold",width=18,bg='#fed51b',fg='black')
            congrat.place(x=135,y=80)
            c.update()
            
            prize1=prize.split(',')
            prize1=''.join(prize1)
            prize1=int(prize1)
            cursor.execute('insert into leaderboard(name,prize)values (%s,%s)',(name[0],prize1,))
            congrat.after(5000)       
            root.destroy()
            fourthcv1.cheque(prize)

    cursor.execute('SELECT  * FROM  questions ORDER BY RAND() LIMIT 1;')
    questionsss=cursor.fetchone()
    a='select * from '
    b=questionsss[0]
    print(b)
    c=a+b
    cursor.execute(c)    
    q=cursor.fetchall()
    def askquestion(lvl):
        def lblupdate(lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,lbl10,lbl11):
            if q[lvl][6]=="20,000":
                lbl1.config(bg="#FFD51B",fg="black",text=" 1  ◆    ₹10,000")
            elif q[lvl][6]=="40,000":
                lbl1.config(bg="#0A22B1",fg="white") 
                lbl2.config(bg="#FFD51B",fg="black",text=" 2  ◆    ₹20,000")
            elif q[lvl][6]=="80,000":
                lbl2.config(bg="#0A22B1",fg="white") 
                lbl3.config(bg="#FFD51B",fg="black",text=" 3  ◆    ₹40,000") 
            elif q[lvl][6]=="1,60,000":
                lbl3.config(bg="#0A22B1",fg="white")
                lbl4.config(bg="#FFD51B",fg="black",text=" 4  ◆    ₹80,000")
            elif q[lvl][6]=="3,20,000":
                lbl4.config(bg="#0A22B1",fg="white") 
                lbl5.config(bg="#FFD51B",fg="black",text=" 5  ◆    ₹1,60,000")
            elif q[lvl][6]=="6,40,000":
                lbl5.config(bg="#0A22B1",fg="white") 
                lbl6.config(bg="#FFD51B",fg="black",text=" 6  ◆    ₹3,20,000")
            elif q[lvl][6]=="12,50,000":
                lbl6.config(bg="#0A22B1",fg="white") 
                lbl7.config(bg="#FFD51B",fg="black",text=" 7  ◆    ₹6,40,000")
            elif q[lvl][6]=="25,00,000":
                lbl7.config(bg="#0A22B1",fg="white") 
                lbl8.config(bg="#FFD51B",fg="black",text=" 8  ◆    ₹12,50,000")
            elif q[lvl][6]=="50,00,000":
                lbl8.config(bg="#0A22B1",fg="white") 
                lbl9.config(bg="#FFD51B",fg="black",text=" 9  ◆    ₹25,00,000")
            elif q[lvl][6]=="1 Crore":
                lbl9.config(bg="#0A22B1",fg="white") 
                lbl10.config(bg="#FFD51B",fg="black",text="10  ◆    ₹50,00,000")
        lblupdate(lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,lbl10,lbl11)
        Question1.set(q[lvl][0])
        Answer1.set(q[lvl][1])
        Answer2.set(q[lvl][2])
        Answer3.set(q[lvl][3])
        Answer4.set(q[lvl][4])
        Canswer.set(q[lvl][5])
        a=q[lvl][1]
        b=q[lvl][2]
        c=q[lvl][3]
        d=q[lvl][4]
        f=q[lvl][5]
        a=a[4:]
        b=b[4:]
        c=c[4:]
        d=d[4:]    
        btn1.config(command=checkans(lvl,btn1,a,f))
        btn2.config(command=checkans(lvl,btn2,b,f))
        btn3.config(command=checkans(lvl,btn3,c,f))
        btn4.config(command=checkans(lvl,btn4,d,f))
            
    def checkans(lvl,btn,a,f):
        prize=q[lvl-1][6]
        if a==f:
            if lvl==0:
                prize='10,000'
                btn.config(command=lambda:[rightanswer(btn,prize),askquestion(lvl+1)])
            if lvl==10:
                prize='₹1 Crore'
                btn.config(command=lambda:[rightanswer(btn,prize)])
            else:    
                btn.config(command=lambda:[rightanswer(btn,prize),askquestion(lvl+1)])        
        else:
            if lvl==0:
                prize='₹0'
            btn.config(command=lambda:[wronganswer(btn,prize)])
    askquestion(0)


    c = Canvas(root,bg="#324AEE", width=810, height=190,highlightthickness=0)
    c.place(x=109,y=367)
    c.create_image(405,105,image=img2)
    c1 = Canvas(root,bg="#324AEE", width=112, height=320,highlightthickness=0)
    c1.place(x=0,y=448)
    c1.create_line(0,33,112,33,fill="#FFD51B",width=4)
    c1.create_line(0,170,112,170,fill="#FFD51B",width=4)
    c1.create_line(0,275,112,275,fill="#FFD51B",width=4)
    c2 = Canvas(root,bg="#324AEE", width=110, height=450,highlightthickness=0)
    c2.place(x=918,y=448)
    c2.create_line(0,35,112,35,fill="#FFD51B",width=4)
    c2.create_line(0,172,112,172,fill="#FFD51B",width=4)
    c2.create_line(0,277,112,277,fill="#FFD51B",width=4)
    c4=Canvas(root,bg='#324AEE',width=1025,height=130,highlightthickness=0)
    c4.place(x=1,y=290)
    Canvas(root,bg="#324AEE", width=810, height=190,highlightthickness=0)
    c.place(x=109,y=367)

    
    txtQuestion=Message(c,justify="center",bg="#0A22B1",bd=0,fg="white",font="Courier 12 bold",aspect=800,textvariable=Question1)
    txtQuestion.place(x=135,y=60,width=550,height=100)
    """
    txtQuestion=Message(c,bg="#0A22B1",bd=0,fg="white",font="Courier 15 bold",height=3,width=35,wrap='word')
    txtQuestion.place(x=140,y=70)"""

    root.mainloop()
    db.commit()
    db.close()
    
