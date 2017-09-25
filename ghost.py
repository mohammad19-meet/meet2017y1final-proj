import random
import time
import turtle
turtle.title("foogho - single player mode")
turtle.tracer(1,0)
#cloning enemy and stage(optional)
enemy = turtle.clone()
stage2 = turtle.clone()
#hiding the enemy, stage turtles
stage2.ht()
enemy.st()
enemy.penup()
#starting position of the enemy
enemy.goto(200,-100)
#registering shapes
turtle.register_shape("ghost_F.gif")
enemy.shape("ghost_F.gif")
turtle.register_shape("ghost.gif")
turtle.register_shape("player_F.gif")
turtle.register_shape("player.gif")
turtle.shape("player.gif")
        
vil_pos = []
vill_tup = (400,400)
vil_pos.append(vill_tup)

#screan size
SIZE_X = 1280
SIZE_Y = 720
turtle.setup(SIZE_X, SIZE_Y)
#square size
SQUARE_SIZE = 20
SQUARE_SIZE1 = 20
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
direction_list = []


#check if the player has food or not
if_player_food = False
#setting direction values
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
#starting directions
direction = UP
gdirection = UP
#cloning the turtle to score
score = turtle.clone()
score.hideturtle()
#position of the score
score.goto(SIZE_X/2-250, SIZE_Y/2 - 100)
#color
score.pencolor("white")
#the score count
count = 0
#score output
score.write("score: " +str(count),font=("Arial", 28, "normal"))
#cloning the village
village = turtle.clone()
turtle.register_shape("village.gif")
village.shape("village.gif")
village.penup()
village.ht()


village.goto(0,-300)
#directions functions for the player
def up():
    global direction
    direction = UP
    print("UP")
    direction_list.append(direction)


def down():
    global direction
    direction = DOWN

    print("DOWN")
    direction_list.append(direction)


def right():
    global direction
    direction = RIGHT
    direction_list.append(direction)


    print("RIGHT")
def left():
    global direction
    direction = LEFT
    direction_list.append(direction)


#direction functions for the enemy
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
#the function of moving the ghost randomly, basicly anything to deal with the ghost
def move_ghost():
    global TIME_STEP, direction,gdirection, SQUARE_SIZE, SQUARE_SIZE1
    #getting updated position of x and y of the ghost
    en_pos = enemy.pos()
    en_x_pos = en_pos[0]
    en_y_pos = en_pos[1]
    #selecting the number that will choose the direction
    randNum = (random.random()) * 100
    if if_player_food == False:
        SQUARE_SIZE1 = 20
        if randNum <= 25 :
            gdirection = UP
        elif randNum >= 25 and randNum<=50:
            gdirection = DOWN

        elif randNum >= 50 and randNum<= 75:
            gdirection = RIGHT
        elif randNum >= 75:
            gdirection = LEFT
    #what happens if player has the food
    if if_player_food == True:
        #making the enemy go to the last direction of the player
        gdirection = direction_list[-2]
        #making the player faster
        SQUARE_SIZE1 = 40
    #making the ghost actually move on the screan by the direction it got
    if gdirection == UP:
        enemy.goto(en_x_pos, en_y_pos + (1.5*SQUARE_SIZE1))
    if gdirection == DOWN:
        enemy.goto(en_x_pos, en_y_pos - (1.5*SQUARE_SIZE1))
    if gdirection == RIGHT:
        enemy.goto(en_x_pos + (1.5*SQUARE_SIZE1), en_y_pos)
    if gdirection == LEFT:
        enemy.goto(en_x_pos - (1.5*SQUARE_SIZE1), en_y_pos)
        en_pos = enemy.pos()
        enemy_pos_list.append(en_pos)
    #what happens if the ghost touches the borders
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
    turtle.ontimer(move_ghost, TIME_STEP)

turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.listen()

#moving the player
def move_player():
    global village, if_player_food, direction, gdirection
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    def ghostChase():
        if direction == RIGHT:
            enemy.goto(x_pos + (1.5*SQUARE_SIZE), y_pos)
        #print("you moved to the right!")
        elif direction == LEFT:
            enemy.goto(x_pos - (1.5*SQUARE_SIZE), y_pos)
        #print("you moved to the left!")
        elif direction == UP:
            enemy.goto(x_pos, y_pos + (1.5*SQUARE_SIZE))
        #print("you moved UP")
        elif direction == DOWN:
            enemy.goto(x_pos, y_pos - (1.5*SQUARE_SIZE))
        turtle.ontimer(ghostChase, TIME_STEP)
                
            
        
    
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
    if if_player_food == True:
        enemy.shape("ghost.gif")
        turtle.shape("player_F.gif")
    elif if_player_food == False:
        enemy.shape("ghost_F.gif")
        turtle.shape("player.gif")
    if -30 <enemy.pos()[0] - turtle.pos()[0] < 30 and -30 < enemy.pos()[1] - turtle.pos()[1] < 30 and if_player_food == False:
        
        
        village.st()
        enemy.goto(0,0)
        time.sleep(0.5)

        #updating player with food status
        if_player_food = True

            

    
    if -40 <enemy.pos()[0] - turtle.pos()[0] < 40 and -40 < enemy.pos()[1] - turtle.pos()[1] < 40 and if_player_food == True:
        score.clear()
        count -=100
        scores.append(count)
        score.pencolor("white")

        score.write("score: "+str(count),font=("Arial", 28, "normal"))
        if_player_food = False
        enemy.goto(0,0)
        time.sleep(0.2)

    if (-15 <village.pos()[0] - turtle.pos()[0] < 15 and -15 < village.pos()[1] - turtle.pos()[1] < 15) and if_player_food == True:
        

            



            score.clear()
            count +=100
            scores.append(count)
            score.pencolor("white")
            score.write("score: "+str(count),font=("Arial", 28, "normal"))
            
            enemy.shape("ghost_F.gif")
            turtle.shape("player.gif")
            if_player_food = False
    if count < 0:
        turtle.goto(0,0)
        turtle.pencolor("white")
        turtle.write("Ghost won!", font = ("Ariel", 28,"normal"))
        time.sleep(5)
        quit()
    
    if count == 1000:
        turtle.goto(0,0)
        turtle.pencolor("white")
        turtle.write("PLayer won!", font = ("Ariel", 28,"normal"))
        time.sleep(5)
        quit()
        



    turtle.ontimer(move_player,TIME_STEP)

def going_menu():
    time.sleep(5)
turtle.onkeypress(going_menu, "p")
turtle.listen()
 
        

