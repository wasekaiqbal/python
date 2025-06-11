'''
print("DRAWING POLYGONS ")
import turtle 
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(700,700) # screen size
polygon = turtle.Turtle()

num_sides = 6
side_length = 100 # shape size
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle) #setting angle
    polygon.speed(1) # setting speed of drawing

turtle.done '''

'''
print("Drawing star")
import turtle 
turtle.Screen().bgcolor("pink")
board= turtle.Turtle()
board.forward(100)

board.left(120) #180-60 (as equilateral triangle)
board.forward(100)

board.left(120) #180-60 (as equilateral triangle)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#2nd triangle

board.pendown()
board.right(90)
board.forward(100)

board.right(120) #180-60 (as equilateral triangle)
board.forward(100)

board.right(120) #180-60 (as equilateral triangle)
board.forward(100)'''

print("optical illusion")
import turtle 
turtle.Screen().bgcolor("purple")
turtle.speed(3)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()
