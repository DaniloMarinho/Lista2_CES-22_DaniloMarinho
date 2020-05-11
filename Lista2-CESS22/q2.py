import turtle # Tess becomes a traffic light.
import time # Timer

wn = turtle.Screen()
wn.setup(400,500)
wn.title("Tess becomes a traffic light!")

wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

#tempo de espera em ms
wait = 1

def advance_state_machine():
    time.sleep(wait)
    tess.forward(70)
    tess.fillcolor("orange")
    time.sleep(wait)
    tess.forward(70)
    tess.fillcolor("red")
    time.sleep(wait)
    
advance_state_machine()
wn.listen() # Listen for events
turtle.mainloop()