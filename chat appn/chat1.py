import socket
import time
import threading
from tkinter import *

root=Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
    t=threading.Thread(target=recv)
    t.start()

def recv():
    listensocket=socket.socket()
    port=8080
    maxconnection=99
    ip=socket.gethostname()

    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()

    while(True):
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbox.insert(0,"Client : "+sendermessage) 

s=0
def sendmsg():
    global s
    if s==0:
        s=socket.socket()
        hostname='DESKTOP-I0HSB7S'
        port=8080
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbox.insert(msg.encode())
        s.send(msg.encode())

    else:
        msg=messagebox.get()
        lstbox.insert(0,"You : "+msg)
        s.send(msg.encode())




def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()
    

startchatimg=PhotoImage(file='download1.png')

buttons=Button(root, image=startchatimg, command=func,borderwidth=0)
buttons.place(x=90,y=10)


message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'), border=2,width=32)
messagebox.place(x=10,y=444)

sendmsgimg=PhotoImage(file='send.png')
sendmsgbtn=Button(root, image=sendmsgimg, command=threadsendmsg,borderwidth=0)
sendmsgbtn.place(x=250,y=430)

lstbox=Listbox(root,height=20,width=43)
lstbox.place(x=15,y=80)

root.mainloop()
