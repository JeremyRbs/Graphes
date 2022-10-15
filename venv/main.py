# coding: utf-8

import tkinter as tk
from tkinter import *
from tkinter import messagebox

from time import strftime
from Windows.home import Graphes
from Algorithms.pcc import *

# Main permettant de lancer le programme
if __name__ == "__main__":

    d = {}
    d = dictionary(d)
    #print(d)

    app = Graphes()
    app.mainloop()
