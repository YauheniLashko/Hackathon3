from turtle import *
from random import randint, choice

screen = Screen()
screen.bgcolor("#86E3F7")
speed(-1)
plant_coor = ((-420, -120), (-300, -240), (150, -300))
seaweed_coor = ((-350, -200), (-390, -250), (-330, -360), (-100, -200), (-130, -270),
                (-30, -240), (10, -220), (60, -300), (250, -370), (320, -320))


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


def draw_fish():
    left(30)
    forward(20)
    right(90)
    circle(50, 120)

    circle(-50, 160)


#draw_fish()

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
mainloop()
