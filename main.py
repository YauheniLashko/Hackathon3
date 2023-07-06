from turtle import *
from random import randint, choice

screen = Screen()
screen.bgcolor("#86E3F7")
speed(-1)
plant_coor = ((-420, -120), (-300, -240), (150, -300))
seaweed_coor = ((-350, -200), (-390, -250), (-330, -360), (-100, -200), (-130, -270),
                (-30, -240), (10, -220), (60, -300), (250, -370), (320, -320))
fish_coor =((300, -200),(-400, 300), (-350, 250))
bubble_coor =((30,300),(90, 350), (10, 370), (-170, 50), (-230, 70), (-190, 160), (10,40), (140, 0), (200, -20), (-360, 390),(-250, 350))
ht()

def do_tp(x,y):
    pu()
    goto(x,y)
    pd()
def draw_sand():
    do_tp(-445, -100)
    color('#ded226')
    begin_fill()
    for i in range(5):
        rt(5)
        fd(200)
    rt(65)
    fd(100)
    rt(90)
    fd(1000)
    end_fill()


def draw_plant(x, y):
    size = randint(30, 80)
    color('#1cb845')
    do_tp(x, y)
    begin_fill()
    for i in range(3):
        circle(size, 180)
        lt(90)
    end_fill()


def draw_seaweed(x, y):
    size = randint(20, 70) #размер водоросли
    direction = choice([-size, size])
    do_tp(x, y)
    color('#006b09')
    pensize(10)
    if direction < 0: #чтобы все водоросли смотрели вверх
        lt(90)
    circle(direction,90)
    circle(-direction, 100)


def draw_fish(x, y):
    pensize(1)
    do_tp(x,y)
    color('#d8ff14')
    begin_fill()
    lt(30)
    fd(20)
    rt(90)
    circle(30, 120)
    lt(90)
    circle(50, 60)
    rt(70)
    fd(25)
    lt(170)
    circle(-20,100)
    end_fill()
    #eyes of fish
    do_tp(xcor()+60, ycor()+15)
    color('black', '#d6d6cb')
    begin_fill()
    circle(4)
    end_fill()
    do_tp(xcor()+2,ycor()-4)
    dot(3)
    # lines on the fish
    do_tp(xcor()-25, ycor()-10)
    color('red')
    lt(180)
    circle(10, 130)
    do_tp(xcor()+10, ycor()+2)
    circle(12,-140)


def draw_dolphin(x,y):
    do_tp(x,y)
    color('#7eaece')
    begin_fill()
    pensize(2)
    coor = pos()
    circle(15,-160)
    lt(180)
    for i in range(9):
        fd(5)
        lt(9)
    for i in range(33):
        fd(i)
        rt(6)
    fd(150)
    for i in range(20):
        bk(i)
        lt(2)
    for i in range(20):
        bk(7)
        lt(1)
    for i in range(20):
        bk(2)
        lt(1)
    for i in range(15):
        bk(3)
        lt(1)
    bk(20)
    end_fill()

    do_tp(coor[0], coor[1])
    color('#E2F4FB')
    lt(30)
    for i in range(10):
        fd(5)
        lt(1)
    color('#daf0ed')
    begin_fill()
    rt(30)
    for i in range(20):
        fd(5)
        rt(2)
    for i in range(20):
        fd(7)
        rt(1)
    for i in range(20):
        fd(2)
        rt(1)
    rt(170)
    color('#7eaece','#E2F4FB')
    circle(200, 30)
    for i in range(15):
        fd(i)
        lt(1)
    for i in range(15):
        fd(3)
        lt(1)
    lt(10)
    for i in range(35):
        fd(1)
        lt(1)
    for i in range(5):
        fd(1)
        rt(7)
    rt(25)
    for i in range(20):
        fd(1)
        rt(2)
    end_fill()
    #рисуем улыбку
    color('#4d4e57')
    pensize(4)
    rt(100)
    circle(100, 30)
    lt(60)
    for i in range(10):
        fd(1)
        rt(1)
    for i in range(20):
        bk(1)
        lt(1)
    #рисуем глаза
    do_tp(xcor()+20, ycor()+40)
    color('white')
    begin_fill()
    circle(10)
    end_fill()
    do_tp(xcor()-10, ycor()-10)
    color('#4d4e57')
    dot(15)
    do_tp(xcor()+17, ycor()+20)
    circle(10,90)
    #рисуем плавник верхний
    do_tp(xcor()+180, ycor()+20)
    color('#7eaece')
    begin_fill()
    lt(180)
    for i in range(20):
        fd(7)
        rt(3)
    for i in range(20):
        fd(2)
        rt(4)
    rt(90)
    circle(60, 130)
    end_fill()
    do_tp(xcor()-160, ycor()+40)
    #плавник нижний, ближний
    rt(30)
    begin_fill()
    for i in range(20):
        fd(5)
        lt(2)
    for i in range(10):
        fd(2)
        lt(5)
    fd(10)
    lt(100)
    for i in range(20):
        fd(3)
        rt(2)
    end_fill()
    #плавник дальний
    do_tp(xcor()-110, ycor()+12)
    rt(130)
    begin_fill()
    for i in range(10):
        fd(3)
        lt(2)
    for i in range(10):
        fd(2)
        lt(5)
    fd(10)
    lt(100)
    for i in range(9):
        fd(3)
        rt(1)
    end_fill()
    #хвост-плавник
    do_tp(xcor()+162, ycor()-190)
    rt(180)
    begin_fill()
    for i in range(20):
        fd(3)
        rt(2)
    for i in range(10):
        fd(3)
        lt(i)
    for i in range(10):
        fd(3)
        lt(5)
    for i in range(10):
        fd(2)
        lt(10)
    for i in range(15):
        fd(3)
        rt(i)
    for i in range(10):
        fd(3)
        rt(i)
    for i in range(20):
        fd(1)
        lt(7)
    circle(60,100)
    for i in range(17):
        fd(1)
        rt(2)
    end_fill()

def draw_buble(x,y):
    pensize(1)
    do_tp(x,y)
    color('dark blue','#cbecf2')
    circle(20)
    do_tp(xcor()-20, ycor())
    color('white')
    begin_fill()
    pensize(10)
    fd(1)
    end_fill()




draw_sand()
lt(180)  # черепаха начинает смотреть вправо после sand
for i in range(3):
    draw_plant(plant_coor[i][0], plant_coor[i][1])
    rt(90)


for i in range(10):
    lt(50)  # черепаха начинает смотреть вверх после draw_plant
    draw_seaweed(seaweed_coor[i][0], seaweed_coor[i][1])
    pu()
    home()  # чтобы черепашка после каждой водоросли возвращалась в стандартное положение
    pd()

for i in range(3):
    draw_fish(fish_coor[i][0], fish_coor[i][1])
    rt(20) # поворачиваем, чтобы следующие рыбки рисовались в нужном направлении"""

draw_dolphin(0,180)

for i in range(11):
    draw_buble(bubble_coor[i][0], bubble_coor[i][1])

mainloop()
