from tkinter import *

root = Tk()
root.geometry('200x100')

b = Button(root, text="Supprime moi", command=lambda: b.pack_forget())
b.pack(pady=20)

root.mainloop()