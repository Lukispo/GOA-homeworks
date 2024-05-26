from turtle import *


# we want to paint a house
color("purple")
speed(30)
width(7)
# step 1: draw a square
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()


# end of square
# drawing door

begin_fill()
left(90)
forward(70)
color("green")
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()
# end of door
# painting window(1)
penup()
goto(150, 70)
pendown()
color("gray")
begin_fill()
width(3)
left(210)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
# end of window(1)
# Painting window(2)



penup()
goto(45, 69)
pendown()
color("gray")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()




# code is done. house is built









exitonclick()