#!/usr/bin/env python3

# simple example

import tkinter as tk
import time
import random

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
random.shuffle(A)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.newgameButton = tk.Button(self, text='New', command=self.startnewgame)
        self.exitButton = tk.Button(self, text='Exit', command=self.quit)
        self.newgameButton.grid()
        self.exitButton.grid(row=0, column=1)
        # cells
        self.cell_00 = tk.Button(self, text=A.pop(0))
        self.cell_01 = tk.Button(self, text=A.pop(0))
        self.cell_02 = tk.Button(self, text=A.pop(0))
        self.cell_03 = tk.Button(self, text=A.pop(0))
        self.cell_10 = tk.Button(self, text=A.pop(0))
        self.cell_11 = tk.Button(self, text=A.pop(0))
        self.cell_12 = tk.Button(self, text=A.pop(0))
        self.cell_13 = tk.Button(self, text=A.pop(0))
        self.cell_20 = tk.Button(self, text=A.pop(0))
        self.cell_21 = tk.Button(self, text=A.pop(0))
        self.cell_22 = tk.Button(self, text=A.pop(0))
        self.cell_23 = tk.Button(self, text=A.pop(0))
        self.cell_30 = tk.Button(self, text=A.pop(0))
        self.cell_31 = tk.Button(self, text=A.pop(0))
        self.cell_32 = tk.Button(self, text=A.pop(0))
        self.cell_00.grid(row=1, column=0)
        self.cell_01.grid(row=1, column=1)
        self.cell_02.grid(row=1, column=2)
        self.cell_03.grid(row=1, column=3)
        self.cell_10.grid(row=2, column=0)
        self.cell_11.grid(row=2, column=1)
        self.cell_12.grid(row=2, column=2)
        self.cell_13.grid(row=2, column=3)
        self.cell_20.grid(row=3, column=0)
        self.cell_21.grid(row=3, column=1)
        self.cell_22.grid(row=3, column=2)
        self.cell_23.grid(row=3, column=3)
        self.cell_30.grid(row=4, column=0)
        self.cell_31.grid(row=4, column=1)
        self.cell_32.grid(row=4, column=2)

    def startnewgame(self):
    	self.createWidgets()
    	
app = Application()
app.master.title('15')
app.mainloop()
