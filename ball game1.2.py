import random
import time
from tkinter import *

level = 0
game_time = 0
tk_level_time = Tk()
tk_level_time.title('难度等级;时间')


def level_up():
    global level
    level = level + 1
    canvas_level_time.delete('all')
    canvas_level_time.create_text(150, 120, text='时间:%s分钟' % game_time, font=('Arial', 30))
    canvas_level_time.create_text(150, 60, text='难度等级:%s级' % level, font=('Arial', 30))


def level_down():
    global level
    if level > 0:
        level = level - 1
        canvas_level_time.delete('all')
        canvas_level_time.create_text(150, 120, text='时间:%s分钟' % game_time, font=('Arial', 30))
        canvas_level_time.create_text(150, 60, text='难度等级:%s级' % level, font=('Arial', 30))


def time_up():
    global game_time
    game_time = game_time + 1
    canvas_level_time.delete('all')
    canvas_level_time.create_text(150, 120, text='时间:%s分钟' % game_time, font=('Arial', 30))
    canvas_level_time.create_text(150, 60, text='难度等级:%s级' % level, font=('Arial', 30))


def time_down():
    global game_time
    if game_time > 0:
        game_time = game_time - 1
        canvas_level_time.delete('all')
        canvas_level_time.create_text(150, 120, text='时间:%s分钟' % game_time, font=('Arial', 30))
        canvas_level_time.create_text(150, 60, text='难度等级:%s级' % level, font=('Arial', 30))


def level_time_sure():
    mark = 0
    start_time = time.time()

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
        now_time = time.time()
        true_game_time = now_time - start_time
        if true_game_time < game_time:
            if ball.hit_bottom == False:
                ball.draw()
                paddle.draw()
                num_time = canvas.create_text(250, 250, text=true_game_time, font=('Arial', 50))
                canvas.delete(num_time)
                num_time = canvas.create_text(250, 250, text=true_game_time, font=('Arial', 50))
            else:
                break
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
            if ball.hit_paddle(ball.canvas.coords(ball.id)) == True:
                mark = mark + 1
            canvas.delete(a)
            a = canvas.create_text(90, 30, text='得分:%s分' % mark, font=('Arial', 30))
        else:
            break
    tk.quit()


bt = Button(tk_level_time, text='难度等级+1', command=level_up)
bt.pack()
bt2 = Button(tk_level_time, text='难度等级-1', command=level_down)
bt2.pack()
bt3 = Button(tk_level_time, text='确定', command=level_time_sure)
bt3.pack()
bt = Button(tk_level_time, text='时间+1分钟', command=time_up)
bt.pack()
bt2 = Button(tk_level_time, text='时间-1分钟', command=time_down)
bt2.pack()

canvas_level_time = Canvas(tk_level_time, width=300, height=180, bd=0, bg='yellow')
canvas_level_time.pack()
tk_level_time.mainloop()
