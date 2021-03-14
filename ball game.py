import random
import time
from tkinter import *

level = int(eval(input('难度等级(1-10):')))
print('记得在弹出页面时单击一下哦!')
time.sleep(1)
mark = 0


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = level
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -level
        if pos[0] <= 0:
            self.x = level
        if pos[2] >= self.canvas_width:
            self.x = -level


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3


tk = Tk()
tk.title('Ball game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, bg='white')
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'yellow')
ball = Ball(canvas, paddle, 'blue')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if ball.hit_paddle(ball.canvas.coords(ball.id)) == True:
        mark = mark + 1
print('游戏结束,你的得分是%s分!'%mark)