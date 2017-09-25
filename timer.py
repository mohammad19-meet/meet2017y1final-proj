import ghost2p
import time
choose = 50*151.515151515


def countdown(n):
    global SIZE_X, SIZE_Y,choose, number
    while n > 0:
        seconds = n/151.515151515

        print (n)
        n = n - 1
        seconds = n/151.515151515

        
        
        ghost2p.countdownT.clear()
        ghost2p.countdownT.pencolor("white")
        ghost2p.countdownT.write(str(int(seconds)), font=("Ariel", 18, "normal"))
        if seconds<=0:
            ghost2p.countdownT.clear()
            ghost2p.countdownT.penup()
            ghost2p.countdownT.goto(0,0)
            ghost2p.countdownT.pendown()
            ghost2p.countdownT.pencolor("white")
            ghost2p.countdownT.write("Player won!", font=("Ariel", 48, "normal"))
            time.sleep(3)
            quit()
