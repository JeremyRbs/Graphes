from tkinter import *


a = Tk()

canvas = Canvas(a, width = 500, height = 500)
canvas.pack()

myrect = canvas.create_rectangle(0,0,100,100)
canvas.delete(myrect) #Deletes the rectangle