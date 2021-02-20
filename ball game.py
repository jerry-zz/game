import time
from tkinter import *


class Ball:
    def __init__(self, canvas, colour):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=colour)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        self.canvas.move(self.id, 0, -1)


tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
ball = Ball(canvas, 'red')
tk.mainloop()

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
