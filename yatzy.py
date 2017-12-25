from tkinter import *
from random import randint
import os

def callback1():
    print(str(randint(1,6)))

def callback2():
    print(str(randint(1, 6))+ ' ' + str(randint(1,6)))

def callback3():
    print(str(randint(1, 6))+ ' ' +str(randint(1,6))+ ' ' +str(randint(1,6)))

def callback4():
    print(str(randint(1, 6))+ ' ' +str(randint(1,6))+ ' ' +str(randint(1,6))+ ' ' +str(randint(1,6)))

def callback5():
    print(str(randint(1, 6))+ ' ' +str(randint(1,6))+ ' ' +str(randint(1,6))+ ' ' +str(randint(1,6))+ ' ' +str(randint(1,6)))

def cls():
    os.system('cls' if os.name=='nt' else 'clear')




top = Tk()
frame = Frame()
frame.pack()

b1 = Button(frame, text="1 terning",width = '30', height = '5', command=callback1)
b2 = Button(frame, text="2 terninger", width = '30', height = '5',command=callback2)
b3 = Button(frame, text="3 terninger", width = '30', height = '5',command=callback3)
b4 = Button(frame, text="4 terninger", width = '30', height = '5',command=callback4)
b5 = Button(frame, text="5 terninger",width = '30', height = '5', command=callback5)
b6 = Button(frame, text="clear console",width = '30', height = '5', command = cls)

b1.pack(side = "left")
b2.pack(side = "left")
b3.pack(side = "left")
b4.pack(side = "left")
b5.pack(side = "left")
b6.pack(side = "right")

top.mainloop()