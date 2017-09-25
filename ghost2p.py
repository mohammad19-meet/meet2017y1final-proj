import random
import time
import turtle
countdownT = turtle.clone()
countdownT.ht()
turtle.tracer(1,0)
enemy = turtle.clone()
enemy.st()
enemy.penup()
enemy.goto(200,-100)
turtle.register_shape("ghost.gif")
enemy.shape("ghost.gif")
does_player_have_food= False
import timer
def check_time():
    if timer.choose == 0:
        countdownT.clear()
        countdownT.penup()
        countdownT.goto(0,0)
        countdownT.pendown()
        countdownT.pencolor("white")
        countdownT.write("Player won!", font=("Ariel", 48, "normal"))
        time.sleep(3)
        quit()
        turtle.ontimer(check_time, TIME_STEP)

#enemy.shape("circle")
#screan size
SIZE_X = 1280
SIZE_Y = 800
turtle.setup(SIZE_X, SIZE_Y)

countdownT.penup()
countdownT.goto(SIZE_X/2-190, SIZE_Y/2 - 100)
countdownT.pendown()
#setting count down
time1 =countdownT.clone()
time1.goto(SIZE_X/2-250, SIZE_Y/2 - 100)
time1.pencolor("white")
time1.write("time: " , font=("Ariel", 18, "normal"))

#square size
SQUARE_SIZE = 20
#doing the borders
def draw_box():
    box = turtle.clone()
    #disign box
    turtle.bgpic("forest.png")
    box.pencolor("green")
    box.penup()
    box.goto(SIZE_X/2, SIZE_Y/2)
    box.pendown()
    box.goto(SIZE_X/2,-SIZE_Y/2)
    box.goto(-SIZE_X/2, -SIZE_Y/2)
    box.goto(-SIZE_X/2, SIZE_Y/2)
draw_box()
#installing arrows
UP_ARROW = "Up"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
LEFT_ARROW = "LEFT"
TIME_STEP = 100
#lists
pos_list = []
enemy_pos_list = []
turtle.penup()
scores = []

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

direction = UP
gdirection = UP
turtle.register_shape("player_F.gif")
turtle.shape("player_F.gif")
score = turtle.clone()
score.hideturtle()

count = 0
village = turtle.clone()
turtle.register_shape("village.gif")
village.shape("village.gif")
village.penup()
village.ht()
randNum1 = (random.random()) * 100
randNum2 = (random.random()) * 100
if randNum1 <= 100:
    randNum1 = (random.random()) * 100
if randNum2 <= 100:
    randNum2 = (random.random()) * 100



village.goto(-400,-300)
def up():
    global direction
    direction = UP
    print("UP")

def down():
    global direction
    direction = DOWN

    print("DOWN")

def right():
    global direction
    direction = RIGHT

    print("RIGHT")

def left():
    global direction
    direction = LEFT
def gup():
    global gdirection
    gdirection = UP
def gdown():
    global gdirection
    gdirection = DOWN
def gleft():
    global gdirection
    gdirection = LEFT
def gright():
    global gdirection
    gdirection = RIGHT
turtle.onkeypress(gup, "w")
turtle.onkeypress(gdown, "s")
turtle.onkeypress(gleft, "a")
turtle.onkeypress(gright, "d")
turtle.onkeypress(gup, "W")
turtle.onkeypress(gdown, "S")
turtle.onkeypress(gleft, "A")
turtle.onkeypress(gright, "D")


def move_ghost():
    global TIME_STEP
    en_pos = enemy.pos()
    en_x_pos = en_pos[0]
    en_y_pos = en_pos[1]

    if gdirection == UP:
        enemy.goto(en_x_pos, en_y_pos + (1.5*SQUARE_SIZE))
    if gdirection == DOWN:
        enemy.goto(en_x_pos, en_y_pos - (1.5*SQUARE_SIZE))
    if gdirection == RIGHT:
        enemy.goto(en_x_pos + (1.5*SQUARE_SIZE), en_y_pos)
    if gdirection == LEFT:
        enemy.goto(en_x_pos - (1.5*SQUARE_SIZE), en_y_pos)
        en_pos = enemy.pos()
        enemy_pos_list.append(en_pos)
    if en_x_pos >= SIZE_X/2:
        enemy.ht()
        enemy.goto(-SIZE_X/2+2, en_y_pos)
        enemy.showturtle()

    elif en_x_pos <= -SIZE_X/2:
        enemy.ht()
        enemy.goto(SIZE_X/2-2, en_y_pos)
        enemy.showturtle()

    elif en_y_pos >= SIZE_Y/2:
        enemy.ht()
        enemy.goto(en_x_pos, -SIZE_Y/2+2)
        enemy.showturtle()

    elif en_y_pos <= -SIZE_Y/2:
        enemy.ht()
        enemy.goto(en_x_pos, SIZE_Y/2-2)
        enemy.showturtle()
    turtle.ontimer(move_ghost, TIME_STEP - 10)

turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.listen()
if_player_food = False

def move_player():
    global village, if_player_food
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction == RIGHT:
        turtle.goto(x_pos + (1.5*SQUARE_SIZE), y_pos)
        #print("you moved to the right!")
    elif direction == LEFT:
        turtle.goto(x_pos - (1.5*SQUARE_SIZE), y_pos)
        #print("you moved to the left!")
    elif direction == UP:
        turtle.goto(x_pos, y_pos + (1.5*SQUARE_SIZE))
        #print("you moved UP")
    elif direction == DOWN:
        turtle.goto(x_pos, y_pos - (1.5*SQUARE_SIZE))
        #print("you moved DOWN")
    my_pos = turtle.pos()
    pos_list.append(my_pos)
    #print(pos_list[-1])
    global TIME_STEP
    global count
        
    #limiting the player in the border
    if x_pos > SIZE_X/2:
        turtle.ht()
        turtle.goto(-SIZE_X/2 + 10, y_pos)
        turtle.st()
    elif x_pos <= -SIZE_X/2:
        turtle.ht()
        turtle.goto(SIZE_X/2, y_pos)
        turtle.st()

    elif y_pos > SIZE_Y/2:
        turtle.ht()
        turtle.goto(x_pos, -SIZE_Y/2+2)
        turtle.st()

    elif y_pos <= -SIZE_Y/2:
        turtle.ht()
        turtle.goto(x_pos, SIZE_Y/2-2)
        turtle.st()
    if -30 <enemy.pos()[0] - turtle.pos()[0] < 30 and -30 < enemy.pos()[1] - turtle.pos()[1] < 30:
        turtle.goto(-100,0)
        turtle.pencolor("white")
        time1.clear()
        turtle.write("ghost won!", font=("Ariel", 48, "normal"))
        time.sleep(5)  
        quit()
           
    turtle.ontimer(move_player,TIME_STEP)


def going_menu():
    time.sleep(5)
turtle.onkeypress(going_menu, "p")
turtle.listen()
 
        

