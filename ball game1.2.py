import random
import time
from tkinter import *

level_OK = False
level = 0
tk2 = Tk()
tk2.title('难度等级')


def A():
    global level
    level = level + 1
    canvas1.delete('all')
    canvas1.create_text(150, 50, text='难度等级:%s级' % level, font=('Arital', 30))


def B():
    global level
    if level > 0:
        level = level - 1
        canvas1.delete('all')
        canvas1.create_text(150, 50, text='难度等级:%s级' % level, font=('Arital', 30))


def C():
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
    a = canvas.create_text(80, 30, text='得分:%s分' % mark, font=('Arial', 30))

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
            canvas.delete(a)
            a = canvas.create_text(90, 30, text='得分:%s分' % mark, font=('Arial', 30))
            tk2.quit()


bt = Button(tk2, text='难度等级+1', command=A)
bt.pack()
bt2 = Button(tk2, text='难度等级-1', command=B)
bt2.pack()
bt3 = Button(tk2, text='确定', command=C)
bt3.pack()
canvas1 = Canvas(tk2, width=300, height=100, bd=0, bg='yellow')
canvas1.pack()
tk2.mainloop()
