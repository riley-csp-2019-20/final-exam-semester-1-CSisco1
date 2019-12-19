#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Colin Sisco
#Date
#12/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game                                                    #done
#The turtle should move with the arrow keys (up, down, left and right), and draw        #done
#Space should clear the screen                                                          #done
#o and p should make the pen size bigger and smaller                                    #done
#u should pick the pen up or put the pen down                                           #done
#All code must be commented
#BONUS
#Add a feature to change colors                                                         #done
#

#import required libraries
import turtle as trtl

#create turtle
drawer = trtl.Turtle()
drawer.shape("turtle")

#variables
pensize = 1
penup_down = 1
wn = trtl.Screen()

#movement functions
def up():
    drawer.setheading(90)
    drawer.forward(15)

def down():
    drawer.setheading(270)
    drawer.forward(15)

def left():
    drawer.setheading(180)
    drawer.forward(15)

def right():
    drawer.setheading(360)
    drawer.forward(15)


#color/drawing functions

def reset_button():
    drawer.color("white")
    drawer.speed(0)
    drawer.pensize(10000)
    drawer.forward(200)
    drawer.back(400)
    drawer.forward(200)
    drawer.speed(1)
    drawer.pensize(pensize)
    drawer.color("black")
    

def pen_bigger():
    global pensize
    pensize = pensize + 1
    drawer.pensize(pensize)

def pen_smaller():
    global pensize
    pensize = pensize - 1
    drawer.pensize(pensize)

def pen_up_down():
    global penup_down
    if penup_down <= 1:
        drawer.penup()
        penup_down = 2
    else:
        drawer.pendown()
        penup_down = 1

#BONUS color functions

def red():
    drawer.color("red")
def green():
    drawer.color("green")
def blue():
    drawer.color("blue")
def default_color():
    drawer.color("black")




#create screen

#bind to keypresses
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(pen_smaller,"o")
wn.onkeypress(pen_bigger,"p")
wn.onkeypress(pen_up_down,"u")
wn.onkeypress(reset_button,"space")
# BONUS different colors
wn.onkeypress(red,"r")
wn.onkeypress(green,"g")
wn.onkeypress(blue,"b")
wn.onkeypress(default_color,"d")


#listen
wn.listen()

#mainloop
wn.mainloop()