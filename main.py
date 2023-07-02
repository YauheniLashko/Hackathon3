from turtle import *
from random import randint, choice

screen = Screen()
screen.bgcolor("#86E3F7")
speed(-1)
plant_coor = ((-420, -120), (-300, -240), (150, -300))
seaweed_coor = ((-350, -200), (-390, -250), (-330, -360), (-100, -200), (-130, -270),
                (-30, -240), (10, -220), (60, -300), (250, -370), (320, -320))
fish_coor =((300, -200),)
hideturtle()
def draw_sand():
    penup()
    goto(-445, -100)
    pendown()
    color('#ded226')
    begin_fill()
    for i in range(5):
        right(5)
        for j in range(40):
            forward(5)
    right(65)
    forward(100)
    right(90)
    forward(1000)
    end_fill()


def draw_plant(x, y):
    size = randint(30, 80)
    color('#1cb845')
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(3):
        circle(size, 180)
        left(90)
    end_fill()


def draw_seaweed(x, y):
    size = randint(20, 70) #размер водоросли
    direction = choice([-size, size])
    penup()

    goto(x, y)
    pendown()
    color('#006b09')

    pensize(10)
    if direction < 0:
        left(90)
    circle(direction,90)
    circle(-direction, 100)


def draw_fish(x, y):
    pensize(1)
    penup()
    goto(x,y)
    pendown()
    color('#d8ff14')
    begin_fill()
    left(30)
    forward(20)
    right(90)
    circle(30, 120)
    left(90)
    circle(50, 60)
    right(70)
    forward(25)
    left(170)
    circle(-20,100)
    end_fill()
    #eyes of fish
    penup()
    goto(xcor()+60, ycor()+15)
    pendown()
    color('black', '#d6d6cb')
    begin_fill()
    circle(4)
    end_fill()
    penup()
    goto(xcor()+2,ycor()-4)
    dot(3)
    # lines on the fish
    penup()
    goto(xcor()-25, ycor()-10)
    pendown()
    color('red')
    left(180)
    circle(10, 130)
    penup()
    goto(xcor()+10, ycor()+2)
    pendown()
    circle(12,-140)



draw_sand()
left(180)  # черепаха начинает смотреть вправо после sand
for i in range(3):
    draw_plant(plant_coor[i][0], plant_coor[i][1])
    right(90)


for i in range(10):
    left(50)  # черепаха начинает смотреть вверх после draw_plant
    draw_seaweed(seaweed_coor[i][0], seaweed_coor[i][1])
    penup()
    home()  # чтобы черепашка после каждой водоросли возвращалась в стандартное положение
    pendown()

for i in range(1):
    draw_fish(fish_coor[i][0], fish_coor[i][1])
mainloop()
