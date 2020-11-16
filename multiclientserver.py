import socket
import sys
from _thread import *
import time
import mysql.connector
db=mysql.connector.connect(user="root",password="root",host="localhost",database='kbc')
cursor=db.cursor()
cursor.execute('SELECT  * FROM  fff;')
q=cursor.fetchall()
host = socket.gethostname()
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
names=[]
s.bind((host, port))
s.listen(5)
s.settimeout(25)
print('Waiting for a connection.')
def threaded_client(conn):
    conn.sendall(str(q).encode())
    while True:
        names.append(conn.recv(2048).decode())
        print(names)
        data = conn.recv(2048)
        if not data:
            break
        
    conn.close()
while True:
    try:
        conn, addr = s.accept()
        print('connected to: '+addr[0]+':'+str(addr[1]))
        start_new_thread(threaded_client,(conn,))
    except:
        print('timeout')
        break
names.sort()
print(names[0]+' is the winner of fastest finger first')

