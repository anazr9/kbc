from tkinter import *
from PIL import ImageTk, Image
from time import time, sleep
import mysql.connector
import socket
import ast
import time
def fff():
        start = time.time()
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host=''#Enter the ip address of the host machine where server program is running
        port=9999
        s.connect((host,port))
        questions=s.recv(1024)
        q=questions.decode()
        q=ast.literal_eval(q)
        root = Tk() 
        root.geometry("1366x768")
        root.configure(bg="#324AEE")
        root.resizable(0,0)
        timer=Canvas(root,bg='#324AEE',width=150,height=150,highlightthickness=0)
        timer.place(x=800,y=10)
        timer.create_oval(10,10,150,150,fill='#324AEE',)
        l1=Label(timer,font='Courier 30 bold',bg='#324AEE',fg='white')
        l1.place(x=55,y=50)
        f=q[0][5]
        db=mysql.connector.connect(user="root",password="root",host="localhost",database='kbc')
        cursor=db.cursor()
        cursor.execute('select fname from registration ORDER BY id DESC LIMIT 1;')
        name=cursor.fetchone()

        def sequence():
                seq=Label(c3,bg="#0A22B1",bd=0,fg="white",font="Courier 14",text='The correct sequence is:',anchor='w')
                seq.place(x=1,y=350)
                sequa.config(text=f[0])
                sequb.config(text=f[1])
                sequc.config(text=f[2])
                sequd.config(text=f[3])
                s.close()
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
        global fff
        fff=''
        
        def countdown(count):
            l1['text'] = count
            if count > 0:
                if count <=20:
                    if count>15:
                        btn1.config(state='disabled')
                        btn2.config(state='disabled')
                        btn3.config(state='disabled')
                        btn4.config(state='disabled')
                    Question1.set(q[0][0])
                    state1 = str(btn1['state'])
                    state2 = str(btn2['state'])
                    state3 = str(btn3['state'])
                    state4 = str(btn4['state'])
                if count <=15:
                    Answer1.set(q[0][1])
                    Answer2.set(q[0][2])
                    Answer3.set(q[0][3])
                    Answer4.set(q[0][4])
                    if count>=float(14.9):
                        btn1.config(state='normal')
                        btn2.config(state='normal')
                        btn3.config(state='normal')
                        btn4.config(state='normal')            
                root.after(1000, countdown, count-1)
                f=q[0][5]
            if count==0:
                sequence()
            global fff

            def checka():
                global fff
                fff=fff+'a'
                print(fff)
                btn1.config(state='disabled')
                if fff==f :
                    end = time.time()
                    end=end-5            
                    elapsed = end - start
                    print(elapsed)    
                    s.send((str(elapsed)+': '+name[0]).encode())
                    s.close()

            def checkb():
                global fff
                fff=fff+'b'
                print(fff)
                btn2.config(state='disabled')
                if fff==f :
                    end = time.time()
                    end=end-6            
                    elapsed = end - start
                    print(elapsed)    
                    s.send((str(elapsed)+': '+name[0]).encode())
                    s.close()


            def checkc():
                global fff
                fff=fff+'c'
                print(fff)
                btn3.config(state='disabled')
                if fff==f :
                    end = time.time()
                    end=end-6
                    elapsed = end - start
                    print(elapsed)    
                    s.send((str(elapsed)+': '+name[0]).encode())
                    s.close()

            def checkd():
                global fff
                fff=fff+'d'
                print(fff)
                btn4.config(state='disabled')
                if fff==f :
                    end = time.time()
                    end=end-6
                    elapsed = end - start
                    print(elapsed)            
                    s.send((str(elapsed)+': '+name[0]).encode())
                    s.close()
            btn1.config(command=lambda:[checka()])
            btn2.config(command=lambda:[checkb()])
            btn3.config(command=lambda:[checkc()])
            btn4.config(command=lambda:[checkd()])
        
        countdown(20)
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

        sequa=Label(c3,bg="#0A22B1",bd=0,fg="#FFD51B",font="Courier 17",anchor='w')
        sequa.place(x=10,y=380)
        sequb=Label(c3,bg="#0A22B1",bd=0,fg="#FFD51B",font="Courier 17",anchor='w')
        sequb.place(x=10,y=410)
        sequc=Label(c3,bg="#0A22B1",bd=0,fg="#FFD51B",font="Courier 17",anchor='w')
        sequc.place(x=10,y=440)
        sequd=Label(c3,bg="#0A22B1",bd=0,fg="#FFD51B",font="Courier 17 ",anchor='w')
        sequd.place(x=10,y=470)

        root.mainloop()
        
