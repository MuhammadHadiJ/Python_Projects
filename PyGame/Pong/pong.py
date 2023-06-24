import turtle
import time

window = turtle.Screen()
window.title("Pong Technology")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# paddle a
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("cyan")
paddle_A.penup()
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.goto(-360 , 0)

# paddle b
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("cyan")
paddle_B.penup()
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.goto(360 , 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("cyan")
ball.penup()
ball.goto(0 , 0)
ball.xs = 0.15
ball.ys = 0.15

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center",font=("Courier", 24, "normal"))

# game loop
def paddle_a_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_a_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_b_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_b_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.xs)
    ball.sety(ball.ycor() + ball.ys)

    if ball.ycor() > 280:
        ball.sety(280)
        ball.ys = -0.15
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.ys = 0.15
    
    if ball.xcor() > 380:
        ball.goto(0, 0)
        time.sleep(1)
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))
        ball.xs = -0.15
    if ball.xcor() < -380:
        ball.goto(0, 0)
        time.sleep(1)
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))
        ball.xs = 0.15

    # paddle collision with the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(340)
        ball.xs = -0.15

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
        ball.setx(-340)
        ball.xs = 0.15