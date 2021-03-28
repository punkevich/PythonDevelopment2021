import tkinter as tk

class Application(tk.Frame):
        
        def __init__(self):
                super().__init__()
                self.frame_text = tk.Frame(self.master, bg = 'grey', bd = 5, width = 840)
                self.frame_graphics = tk.Frame(self.master, bg = 'grey')
                self.frame_exit = tk.Frame(self.master)
                self.canvas = tk.Canvas(self.frame_graphics, bd = 5, bg = 'grey')
                self.button_exit = tk.Button(self.frame_exit, text = 'Exit', command = self.quit)

if __name__ == "__main__":
    App = Application()
    App.mainloop()
