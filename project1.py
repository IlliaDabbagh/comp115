import turtle

alex = turtle.Turtle()
alex2 = turtle.Turtle()
alex3 = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
alex.color("green")
alex2.color("white")
alex3.color("red")

def patern_1(t, screen, x_coordinate, y_coordinate):
    """draw first pattern given turtle, screen, x and y coordinates"""
    t.penup()
    t.goto(x_coordinate, y_coordinate)
    t.pendown()
    a = 0
    b = 0
    t.speed(0)
    while b <= 210:
        t.forward(a)
        t.left(b)
        a += 1
        b += 1

    alex.hideturtle()

def patern_2(tt, wn, x_coordinate, y_coordinate):
    """draw second pattern given turtle, screen, x and y coordinated"""
    tt.penup()
    tt.goto(x_coordinate, y_coordinate)
    tt.pendown()
    tt.speed(0)
    c = 0
    while c <= 360 / 5:
        for i in range(4):
            tt.forward(85)
            tt.right(90)
        tt.right(5)
        c += 1
        tt.hideturtle()

def patern_3(ttt, wn):
    ttt.speed(0)
    for i in range(200):
        ttt.forward(i + 1)
        ttt.left(89)
    ttt.hideturtle()


patern_2(alex2, wn, 220, -200)
patern_2(alex2, wn, -220, 200)
patern_1(alex, wn, -250, -250)
patern_1(alex, wn, 225, 260)
patern_3(alex3, wn)




wn.exitonclick()