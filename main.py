import turtle
import sys


# Screen Setup

win = turtle.Screen()
win.title("Classic Pong Game | codebyimran")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Game State

game_running = False


# Score

score_a = 0
score_b = 0


# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.hideturtle()


# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.hideturtle()


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
ball.hideturtle()


# UI Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()


# MENU UI

def show_menu():
    pen.clear()
    pen.goto(0, 60)
    pen.write("CLASSIC PONG", align="center", font=("Courier", 36, "bold"))

    pen.goto(0, 0)
    pen.write("Press P to Play", align="center", font=("Courier", 18, "normal"))

    pen.goto(0, -40)
    pen.write("Press Q to Quit", align="center", font=("Courier", 18, "normal"))

    pen.goto(0, -240)
    pen.write("Code by imran", align="center", font=("Courier", 18, "normal"))

    paddle_a.hideturtle()
    paddle_b.hideturtle()
    ball.hideturtle()


# START GAME

def start_game():
    global game_running, score_a, score_b
    game_running = True
    score_a = 0
    score_b = 0

    pen.clear()
    pen.goto(0, 250)
    pen.write(
        f"Player A: {score_a}   -   Player B: {score_b}",
        align="center",
        font=("Courier", 24, "normal")
    )

    paddle_a.showturtle()
    paddle_b.showturtle()
    ball.showturtle()
    ball.goto(0, 0)


# EXIT GAME

def exit_game():
    win.bye()
    sys.exit()


# Paddle Movement

def paddle_a_up():
    if game_running and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    if game_running and paddle_a.ycor() > -250:
        paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    if game_running and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    if game_running and paddle_b.ycor() > -250:
        paddle_b.sety(paddle_b.ycor() - 20)


# Keyboard Bindings

win.listen()
win.onkeypress(start_game, "p")
win.onkeypress(exit_game, "q")

win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Show menu first
show_menu()


# Main Loop

while True:
    win.update()

    if not game_running:
        continue

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Scoring
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1

    pen.clear()
    pen.goto(0, 250)
    pen.write(
        f"Player A: {score_a}   -   Player B: {score_b}",
        align="center",
        font=("Courier", 24, "normal")
    )

    # Paddle collision
    if 340 < ball.xcor() < 350 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50:
        ball.dx *= -1

    if -350 < ball.xcor() < -340 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
        ball.dx *= -1

    # Win condition → back to menu
    if score_a == 10 or score_b == 10:
        game_running = False
        show_menu()
