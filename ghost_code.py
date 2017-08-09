
import random
import time
import turtle


turtle.tracer(1,0)
enemy = turtle.clone()
enemy.penup()
enemy.goto(200,0)
turtle.register_shape("ghost_F.gif")
enemy.shape("ghost_F.gif")
does_player_have_food= False

vil_pos = []
vill_tup = (400,400)
vil_pos.append(vill_tup)

#enemy.shape("circle")
#screan size
SIZE_X = 1028
SIZE_Y = 800
turtle.setup(SIZE_X, SIZE_Y)
#square size
SQUARE_SIZE = 20

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

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

direction = UP
gdirection = UP
turtle.register_shape("player.gif")
turtle.shape("player.gif")
score = turtle.clone()
score.hideturtle()
score.write("score: ")
count = 0
village = turtle.clone()
turtle.register_shape("village.gif")
village.shape("circle")
village.penup()
village.ht()
randNum1 = (random.random()) * 100
randNum2 = (random.random()) * 100
if randNum1 <= 100:
    randNum1 = (random.random()) * 100
if randNum2 <= 100:
    randNum2 = (random.random()) * 100



village.goto(randNum1,randNum2)
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

def move_ghost():
    global TIME_STEP
    en_pos = enemy.pos()
    en_x_pos = en_pos[0]
    en_y_pos = en_pos[1]

    randNum = (random.random()) * 100
    if randNum <= 25 :
        gdirection = UP
    elif randNum >= 25 and randNum<=50:
        gdirection = DOWN

    elif randNum >= 50 and randNum<= 75:
        gdirection = RIGHT
    elif randNum >= 75:
        gdirection = LEFT
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
    if en_x_pos >= 514:
        enemy.ht()
        enemy.goto(-512, en_y_pos)
        enemy.showturtle()

    elif en_x_pos <= -514:
        enemy.ht()
        enemy.goto(512, en_y_pos)
        enemy.showturtle()

    elif en_y_pos >= 400:
        enemy.ht()
        enemy.goto(en_x_pos, -398)
        enemy.showturtle()

    elif en_y_pos <= -400:
        enemy.ht()
        enemy.goto(en_x_pos, 398)
        enemy.showturtle()
    turtle.ontimer(move_ghost, TIME_STEP)
move_ghost()

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
    if x_pos >= 514:
        turtle.ht()
        turtle.goto(-512, y_pos)
        turtle.st()
    elif x_pos <= -514:
        turtle.ht()
        turtle.goto(512, y_pos)
        turtle.st()

    elif y_pos >= 400:
        turtle.ht()
        turtle.goto(x_pos, -398)
        turtle.st()

    elif y_pos <= -400:
        turtle.ht()
        turtle.goto(x_pos, 398)
        turtle.st()
    if -15 <enemy.pos()[0] - turtle.pos()[0] < 15 and -15 < enemy.pos()[1] - turtle.pos()[1] < 15:
        turtle.register_shape("ghost.gif")
        enemy.shape("ghost.gif")
        turtle.register_shape("player_F.gif")
        turtle.shape("player_F.gif")
        village.st()
        
        enemy.goto(0,0)
        
        if if_player_food:
            quit()
            

        ## Try to understand me!!!???        
        if_player_food = True
    if (-15 <village.pos()[0] - turtle.pos()[0] < 15 and -15 < village.pos()[1] - turtle.pos()[1] < 15):
        
        enemy.shape("ghost_F.gif")
        turtle.shape("player.gif")
        print("success")
        if if_player_food == True:
            score.clear()
            count +=1
            score.write("scpre: "+str(count))
        if_player_food = False
    
        



    turtle.ontimer(move_player,TIME_STEP)
 
        
    
        
move_player()

