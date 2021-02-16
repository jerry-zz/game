import time
from tkinter import *


class Ball:
    def __init__(self, canvas, colour):
        self.canvas = Canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=colour)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass


tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
tk.mainloop()

ball = Ball(canvas, 'red')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
