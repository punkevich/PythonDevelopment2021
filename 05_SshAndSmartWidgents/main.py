import numpy as np
import tkinter as tk
from functools import partial


class Application(tk.Frame):
        
        def __init__(self):
                self.next_label = 0
                self.labels = list()
                self.texts = list()
                super().__init__()
                self.frame_text = tk.Frame(self.master, bg = 'white', bd = 5, width = 860, height = 760)
                self.frame_graphics = tk.Frame(self.master, bg = 'white')
                self.frame_exit = tk.Frame(self.master)
                self.canvas = tk.Canvas(self.frame_graphics, bd = 5, bg = 'green')
                self.button_exit = tk.Button(self.frame_exit, text = 'Exit', command = self.quit)
                self.master.columnconfigure(0, weight = 1, minsize = 50)
                self.master.columnconfigure(1, weight = 1, minsize = 50)
                self.master.rowconfigure(0, weight = 1, minsize = 50)
                self.master.rowconfigure(1, weight = 0, minsize = 10)
                self.frame_text.columnconfigure((0, 1, 2, 3, 4), weight = 1)
                self.frame_graphics.rowconfigure(0, weight = 1)
                self.frame_graphics.columnconfigure(0, weight = 1)
                self.grid(sticky = tk.NSEW)
                self.frame_text.grid(row = 0, column = 0, sticky = tk.NSEW)
                self.frame_graphics.grid(row = 0, column = 1, sticky = tk.NSEW)
                self.frame_exit.grid(row = 1, column = 1, sticky = tk.NSEW)
                self.canvas.grid(sticky = tk.NSEW)
                self.button_exit.pack(side = 'right')
                self.canvas.bind('<Button-1>', self.create_figure)
                               
        def create_figure(self, event):
                self.canvas.bind('<B1-Motion>', self.change_size)
                self.canvas.bind('<ButtonRelease-1>', self.create_label)

                self.x, self.y = event.x, event.y
                self.current_id = self.canvas.create_oval(self.x, self.y, self.x, self.y, fill = 'yellow')
                self.canvas.tag_bind(self.current_id, '<Button-1>', self.pick_figure)
                self.canvas.tag_bind(self.current_id, '<B1-Motion>', partial(self.move_figure, self.current_id))
                self.canvas.tag_bind(self.current_id, '<ButtonRelease-1>', self.release_figure)
                
        def change_size(self, event):
                self.size_x, self.size_y = event.x, event.y
                self.canvas.coords(self.current_id, self.x, self.y, self.size_x, self.size_y)

        def create_label(self, event):
                self.canvas.unbind('<B1-Motion>')
                self.canvas.unbind('<ButtonRelease-1>')
                label_array = np.zeros((5), dtype = tk.Label)
                text_array = np.zeros((5), dtype = tk.StringVar)
                for i in range(5):
                        text_array[i] = tk.StringVar()
                        label_array[i] = tk.Entry(self.frame_text, bg = 'white', textvariable = text_array[i])
                        label_array[i].grid(row = self.next_label, column = i, sticky = tk.NSEW)
                        label_array[i].bind('<Key>', partial(self.update, self.current_id))

                text_array[0].set('oval')
                text_array[1].set('{} {} {} {}'.format(self.x, self.y, self.size_x, self.size_y))
                text_array[2].set('1')
                text_array[3].set('yellow')
                text_array[4].set('black')
                
                self.next_label += 1
                self.labels.append(label_array)
                self.texts.append(text_array)
                
        def update(self, current_id, event):
                if event.keysym == 'Return':
                        if self.texts[current_id - 1][0].get() == 'oval':
                                self.labels[current_id - 1][0].configure(bg = 'white')
                else:
                        self.labels[current_id - 1][0].configure(bg = 'yellow')

                try:
                        coords = np.array(self.texts[current_id - 1][1].get().split(), dtype = np.int64)
                        self.canvas.coords(current_id, tuple(coords))
                        self.labels[current_id - 1][1].configure(bg = 'white')
                except:
                        self.labels[current_id - 1][1].configure(bg = 'yellow')
                try:
                        width = float(self.texts[current_id - 1][2].get())
                        self.canvas.itemconfigure(current_id, width = width)
                        self.labels[current_id - 1][2].configure(bg = 'white')
                except:
                        self.labels[current_id - 1][2].configure(bg = 'yellow')

                try:
                        color = self.texts[current_id - 1][3].get()
                        self.canvas.itemconfigure(current_id, fill = color)
                        self.labels[current_id - 1][3].configure(bg = 'white')
                except:
                        self.labels[current_id - 1][3].configure(bg = 'yellow')

                try:
                        color = self.texts[current_id - 1][4].get()
                        self.canvas.itemconfigure(current_id, outline = color)
                        self.labels[current_id - 1][4].configure(bg = 'white')
                except:
                        self.labels[current_id - 1][4].configure(bg = 'yellow')
                        
        def pick_figure(self, event):
                self.x, self.y = event.x, event.y
                self.canvas.unbind('<Button-1>') 
                
        def move_figure(self, current_id, event):
                coords = np.array(self.texts[current_id - 1][1].get().split(), dtype = np.int64)
                coords[[0, 2]] += event.x - self.x
                coords[[1, 3]] += event.y - self.y
                self.texts[current_id - 1][1].set('{} {} {} {}'.format(coords[0], coords[1], coords[2], coords[3]))
                self.canvas.move(current_id, event.x - self.x, event.y - self.y)
                self.x, self.y = event.x, event.y
         
        def release_figure(self, event):
                self.canvas.bind('<Button-1>', self.create_figure)                      

if __name__ == "__main__":
    App = Application()
    App.mainloop()
