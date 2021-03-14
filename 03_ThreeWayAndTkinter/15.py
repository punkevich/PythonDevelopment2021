#!/usr/bin/env python3

import tkinter as tk
import time
import random

cells = [[0] * 4 for i in range(4)]

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
        #self.createCells()

    def fillMatrix(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1]
        random.shuffle(A)
        for i in range(4):
                for j in range(4):
                        cells[i][j] = tk.Button(self, text=A.pop(0), width=2)
                        if cells[i][j]["text"] != -1:
                                cells[i][j].grid(row=i+1, column=j)
        
        
    
    def createCells(self):
        
        if (cells[0][0] > 0):
                self.cell_00 = tk.Button(self, text=cells[0][0], width=2)
                self.cell_00.grid(row=1, column=0)
        
        if (cells[0][1] > 0):
                self.cell_01 = tk.Button(self, text=cells[0][1], width=2)
                self.cell_01.grid(row=1, column=1)
        if (cells[0][2] > 0):
                self.cell_02 = tk.Button(self, text=cells[0][2], width=2)
                self.cell_02.grid(row=1, column=2)
        if (cells[0][3] > 0):
                self.cell_03 = tk.Button(self, text=cells[0][3], width=2)
                self.cell_03.grid(row=1, column=3)
        if (cells[1][0] > 0):
                self.cell_10 = tk.Button(self, text=cells[1][0], width=2)
                self.cell_10.grid(row=2, column=0)
        if (cells[1][1] > 0):
                self.cell_11 = tk.Button(self, text=cells[1][1], width=2)
                self.cell_11.grid(row=2, column=1)
        if (cells[1][2] > 0):
                self.cell_12 = tk.Button(self, text=cells[1][2], width=2)
                self.cell_12.grid(row=2, column=2)
        if (cells[1][3] > 0):
                self.cell_13 = tk.Button(self, text=cells[1][3], width=2)
                self.cell_13.grid(row=2, column=3)
        if (cells[2][0] > 0):
                self.cell_20 = tk.Button(self, text=cells[2][0], width=2)
                self.cell_20.grid(row=3, column=0)
        if (cells[2][1] > 0):
                self.cell_21 = tk.Button(self, text=cells[2][1], width=2)
                self.cell_21.grid(row=3, column=1)
        if (cells[2][2] > 0):
                self.cell_22 = tk.Button(self, text=cells[2][2], width=2)
                self.cell_22.grid(row=3, column=2)
        if (cells[2][3] > 0):
                self.cell_23 = tk.Button(self, text=cells[2][3], width=2)
                self.cell_23.grid(row=3, column=3)
        if (cells[3][0] > 0):
                self.cell_30 = tk.Button(self, text=cells[3][0], width=2)
                self.cell_30.grid(row=4, column=0)
        if (cells[3][1] > 0):
                self.cell_31 = tk.Button(self, text=cells[3][1], width=2)
                self.cell_31.grid(row=4, column=1)
        if (cells[3][2] > 0):
                self.cell_32 = tk.Button(self, text=cells[3][2], width=2)
                self.cell_32.grid(row=4, column=2)
        if (cells[3][3] > 0):
                self.cell_33 = tk.Button(self, text=cells[3][3], width=2)
                self.cell_33.grid(row=4, column=3)
    
    def startnewgame(self):
        print(2)
        
    	
app = Application()
app.master.title('15')
app.mainloop()
