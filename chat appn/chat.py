import socket
import time
import threading
from tkinter import *

root=Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
    pass
def threadsendmsg():
    pass

startchatimg=PhotoImage(file='download1.png')

buttons=Button(root, image=startchatimg, command=func,borderwidth=0)
buttons.place(x=-5,y=0)

message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'), border=2,width=32)
messagebox.place(x=10,y=444)

sendmsgimg=PhotoImage(file='send.png')
sendmsgbtn=Button(root, image=sendmsgimg, command=threadsendmsg,borderwidth=0)
buttons.place(x=260,y=440)

lstbox=Listbox(root,height=20,width=43)
lstbox.place(x=15,y=80)

root.mainloop()
