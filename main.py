import tkinter.dnd
from tkinter import *
from tkinter import ttk

import timer
from vpython import *
import time

root = Tk()
root.geometry("250x200")

def start(event):
    print("start")

    print(int(axEntry.get()))

    scene.width = 2000
    scene.height = 1000     
    scene.camera.pos=vector(0,20,40)
    a = vertex(pos = vector(-scene.width, -0.5, scene.width))
    b = vertex(pos = vector(scene.width, -0.5, scene.width))
    d = vertex(pos = vector(-scene.width,-0.5, -scene.width))
    c = vertex(pos = vector(scene.width, -0.5, -scene.width))
    Q = quad(vs=[a,b,c,d])
    sph = sphere(color=color.red, pos=vector(0, 0, 0))
    v0 = int(veEntry.get())

    a = int(axEntry.get())
    T = int(timeEntry.get())
    sec = 0

    while sec <= T:
        rate(100)
        print(sec)
        time.sleep(1)
        sec +=1
        v = v0 + (a * sec)
        s = (a * sec * sec) / 2
        l = vector(s, 0, 0)
        sph.pos = sph.pos + l
        print(v)











StartBtn = Button(root, text="Start")
StartBtn.bind("<Button-1>", start)
StartBtn.pack()
axEntry = Entry()
axEntry.pack(side='bottom')
axEntry.insert(END,'Введите ускорение')
timeEntry = Entry()
timeEntry.insert(END, 'Введите время')
timeEntry.pack(side='left')
veEntry = Entry()
veEntry.insert(END, 'Введите нач.скорость')
veEntry.pack(side='right')
root.mainloop()
