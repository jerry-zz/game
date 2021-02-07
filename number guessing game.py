import random
import time

print('你好,用户.你叫什么名字?')
name = input()
print('哦!你好%s,很高兴认识你.' % name)
time.sleep(0.5)
print('我们来玩个游戏吧!好吗?(Y/N)')
a = input('')
if a == 'Y':
    print('我想到了一个1~100间的数,你来猜一猜.')
    time.sleep(0.5)
    print('你想要几次机会?')
    count = int(input())
    print('好,猜吧!')
    time.sleep(0.5)
    answer = random.randint(1, 101)
    for z in range(count):
        useranswer = eval(input('你猜的数字是:'))
        if useranswer == answer:
            print('正确!')
            win = True
            break
        else:
            if count - 1 - z > 0:
                if useranswer > answer:
                    print('大了!你还有%s次机会.' % (count - 1 - z))
                    time.sleep(0.5)
                    continue
                else:
                    print('小了!你还有%s次机会.' % (count - 1 - z))
                    time.sleep(0.5)
                    continue
            else:
                win = False
    if win == True:
        print('恭喜你%s,你赢了!' % name)
    else:
        print('对不起%s,但是你输了,你没有机会了.' % name)
else:
    print('好吧,那么%s,再见啦!' % name)
