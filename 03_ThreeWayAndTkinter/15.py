#!/usr/bin/env python3

import tkinter as tk
import time
import random

#cells = [[0] * 4 for i in range(4)]
cells = []

class cellButton:
        
        widget = tk.Button(text=1, command=btnClick)
        row = 0
        column = 0
        
        def __init__(self, row, column, value):
                self.row = row
                self.column = column
                self.widget = tk.Button(self, text=value, command=self.btnClick)
                
        def btnClick(self, btn):
                print(self.widget.grid_info()) 

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
        self.fillMatrix()

    def fillMatrix(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1]
        random.shuffle(A)
        for i in range(4):
                for j in range(4):
                        cells.append(cellButton(i,j,A.pop()))
    
    def startnewgame(self):
        print(2)
        
    	
app = Application()
app.master.title('15')
app.mainloop()
