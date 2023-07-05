from turtle import *
from random import randint, choice

screen = Screen()
screen.bgcolor("#86E3F7")
speed(-1)
plant_coor = ((-420, -120), (-300, -240), (150, -300))
seaweed_coor = ((-350, -200), (-390, -250), (-330, -360), (-100, -200), (-130, -270),
                (-30, -240), (10, -220), (60, -300), (250, -370), (320, -320))
fish_coor =((300, -200),(-400, 300), (-350, 250))
#hideturtle()
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


def draw_dolphin(x,y):
    penup()
    goto(x,y)
    pendown()
    color('#7eaece')
    begin_fill()
    pensize(2)
    coor = pos()
    circle(15,-160)
    left(180)
    for i in range(9):
        forward(5)
        left(9)
    for i in range(33):
        forward(i)
        right(6)
    forward(150)
    #color('blue')
    for i in range(20):
        backward(i)
        left(2)
    for i in range(20):
        backward(7)
        left(1)
    for i in range(20):
        backward(2)
        left(1)
    for i in range(15):
        backward(3)
        left(1)
    backward(20)
    end_fill()
    penup()
    goto(coor)
    pendown()
    color('#E2F4FB')
    left(30)
    for i in range(10):
        forward(5)
        left(1)
    color('#daf0ed')
    begin_fill()
    right(30)
    for i in range(20):
        forward(5)
        right(2)
    for i in range(20):
        forward(7)
        right(1)
    for i in range(20):
        forward(2)
        right(1)
    right(170)
    color('#7eaece','#E2F4FB')
    circle(200, 30)
    for i in range(15):
        forward(i)
        left(1)
    for i in range(15):
        forward(3)
        left(1)
    left(10)
    for i in range(35):
        forward(1)
        left(1)
    for i in range(5):
        forward(1)
        right(7)
    right(25)
    for i in range(20):
        forward(1)
        right(2)
    end_fill()
    #рисуем улыбку
    color('#4d4e57')
    pensize(4)
    right(100)
    circle(100, 30)
    left(60)
    for i in range(10):
        forward(1)
        right(1)
    for i in range(20):
        backward(1)
        left(1)
    #рисуем глаза
    penup()
    goto(xcor()+20, ycor()+40)
    pendown()
    color('white')
    begin_fill()
    circle(10)
    end_fill()
    penup()
    goto(xcor()-10, ycor()-10)
    pendown()
    color('#4d4e57')
    dot(15)
    penup()
    goto(xcor()+17, ycor()+20)
    pendown()
    circle(10,90)
    #рисуем плавник верхний
    penup()
    goto(xcor()+180, ycor()+20)
    pendown()
    color('#7eaece')
    begin_fill()
    left(180)
    for i in range(20):
        forward(7)
        right(3)
    for i in range(20):
        forward(2)
        right(4)
    right(90)
    circle(60, 130)
    end_fill()
    goto(xcor()-160, ycor()+40)
    #плавник нижний, ближний
    right(30)
    begin_fill()
    for i in range(20):
        forward(5)
        left(2)
    for i in range(10):
        forward(2)
        left(5)
    forward(10)
    left(100)
    for i in range(20):
        forward(3)
        right(2)
    end_fill()




draw_dolphin(0,0)

"""
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

for i in range(3):
    draw_fish(fish_coor[i][0], fish_coor[i][1])
    right(20) # поворачиваем, чтобы следующие рыбки рисовались в нужном направлении"""
mainloop()
