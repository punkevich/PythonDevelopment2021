import tkinter as tk

class Application(tk.Frame):
        
        def __init__(self):
                super().__init__()
                self.frame_text = tk.Frame(self.master, bg = 'white', bd = 5, width = 860)
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

if __name__ == "__main__":
    App = Application()
    App.mainloop()
