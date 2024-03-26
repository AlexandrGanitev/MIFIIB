import turtle as t
import os

player_a_score: int = 0
player_b_score: int = 0

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5, 5)
ball_x_direction = 0.5
ball_y_direction = 0.5

# code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=("Arial", 24, "normal"))


# code for moving the leftpaddle
def leftpaddleup() :
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sety(y)


def leftpaddledown() :
    y = leftpaddle.ycor()
    y = y - 90
    leftpaddle.sety(y)


# code for moving the rightpaddle
def rightpaddleup() :
    y = rightpaddle.ycor()
    y = y + 90
    rightpaddle.sety(y)


def rightpaddledown() :
    y = rightpaddle.ycor()
    y = y - 90
    rightpaddle.sety(y)


# assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor()+ball_x_direction)
    ball.sety(ball.ycor()+ball_y_direction)

    # border set up
    if ball.ycor()>290:
        ball.sety(290)
        ball_y_direction = ball_y_direction * -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball_y_direction = ball_y_direction * -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}          Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")

    if (ball.xcor()) < -390 :  # left width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    # handling the collisions with paddles.

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40) :
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40) :
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

# This version I found on the Internet, my previous (Coursera Python course) had been more precise, used
# used the coordinates, however, it worked on the canvas of the Codesculptor, so it has to be adjusted
# for the turtle library.

# Implementation of classic arcade game Pong
# Developed by Alexandr Ganitev, on November 29th, 2021

# import simplegui
# import random
#
# # initialize globals - pos and vel encode vertical info for paddles
# WIDTH = 600
# HEIGHT = 400
# BALL_RADIUS = 20
# PAD_WIDTH = 8
# PAD_HEIGHT = 80
# HALF_PAD_WIDTH = PAD_WIDTH / 2
# HALF_PAD_HEIGHT = PAD_HEIGHT / 2
# LEFT = False
# RIGHT = True
# ball_pos = [0, 0]
# ball_vel = [0, 0]
# paddle1_pos = HEIGHT / 2
# paddle2_pos = HEIGHT / 2
# paddle1_vel = 0.0
# paddle2_vel = 0.0
# score1 = 0
# score2 = 0
#
#
# # initialize ball_pos and ball_vel for new ball in middle of table
# # if direction is RIGHT, the ball's velocity is upper right, else upper left
# def spawn_ball(direction) :
#     global ball_pos, ball_vel  # these are vectors stored as lists
#     ball_pos = [WIDTH / 2, HEIGHT / 2]
#     if direction == RIGHT :
#         ball_vel[0] = random.randrange(2, 4)
#     else :
#         ball_vel[0] = - random.randrange(2, 4)
#     ball_vel[1] = - random.randrange(1, 3)
#
#
# # define event handlers
# def new_game() :
#     global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
#     global score1, score2  # these are ints
#     spawn_ball(RIGHT)
#
#
# def draw(canvas) :
#     global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
#
#     # draw mid line and gutters
#     canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
#     canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
#     canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
#     canvas.draw_circle(([WIDTH / 2, HEIGHT / 2]), BALL_RADIUS * 2, 1, "White")
#     # update ball
#     ball_pos[0] += ball_vel[0]
#     ball_pos[1] += ball_vel[1]
#     # for testing purposes:
#     # print "Value of velocity: ", ball_vel[0], ball_vel[1]
#
#     # collide and reflect off of top and bottom walls
#     if ball_pos[1] <= BALL_RADIUS :
#         ball_vel[1] = - ball_vel[1]
#     if ball_pos[1] >= HEIGHT - BALL_RADIUS :
#         ball_vel[1] = - ball_vel[1]
#     # draw ball
#     canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Blue", "Yellow")
#     # updateing paddle's vertical position,
#     # checking if the paddles are not leaving the field and are not sticking to the edges:
#     if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT :
#         paddle1_pos += paddle1_vel
#     if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT :
#         paddle2_pos += paddle2_vel
#     # draw paddles
#     canvas.draw_line([0, (paddle1_pos - HALF_PAD_HEIGHT)], [0, (paddle1_pos + HALF_PAD_HEIGHT)], 14, 'Yellow')
#     canvas.draw_line([WIDTH, (paddle2_pos - HALF_PAD_HEIGHT)], [WIDTH, (paddle2_pos + HALF_PAD_HEIGHT)], 14, 'Yellow')
#
#     # determine whether paddle and ball collide
#     if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH :
#         # testing collision with the paddle1
#         if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT :
#             ball_vel[0] = - 1.1 * ball_vel[0]
#             ball_vel[1] = 1.1 * ball_vel[1]
#         else :
#             score2 += 1
#             spawn_ball(RIGHT)
#     # for testing purposes:
#     # print ball_pos[1], paddle1_pos, paddle2_pos
#     if (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH) :
#         # testing collision with the paddle2:
#         if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT :
#             ball_vel[0] = - 1.1 * ball_vel[0]
#             ball_vel[1] = 1.1 * ball_vel[1]
#         else :
#             score1 += 1
#             spawn_ball(LEFT)
#
#     # draw scores
#     canvas.draw_text(str(score1), [WIDTH / 4, HEIGHT / 8], 30, "Yellow")
#     canvas.draw_text(str(score2), [WIDTH / 4 * 3, HEIGHT / 8], 30, "Yellow")
#
#
# def restart() :
#     global score1, score2
#     score1 = 0
#     score2 = 0
#     new_game()
#
#
# def keydown(key) :
#     global paddle1_vel, paddle2_vel
#     # paddle acceleration
#     acc = 5
#     if key == simplegui.KEY_MAP["w"] :
#         paddle1_vel -= acc
#     elif key == simplegui.KEY_MAP["s"] :
#         paddle1_vel += acc
#     elif key == simplegui.KEY_MAP["up"] :
#         paddle2_vel -= acc
#     elif key == simplegui.KEY_MAP["down"] :
#         paddle2_vel += acc
#
#
# def keyup(key) :
#     global paddle1_vel, paddle2_vel
#     if key == simplegui.KEY_MAP["w"] :
#         paddle1_vel = 0
#     elif key == simplegui.KEY_MAP["s"] :
#         paddle1_vel = 0
#     elif key == simplegui.KEY_MAP["up"] :
#         paddle2_vel = 0
#     elif key == simplegui.KEY_MAP["down"] :
#         paddle2_vel = 0
#
#
# # create frame
# frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
# frame.set_draw_handler(draw)
# frame.set_keydown_handler(keydown)
# frame.set_keyup_handler(keyup)
# frame.add_button("Restart the game", restart)
#
# # start frame
# new_game()
# frame.start()
