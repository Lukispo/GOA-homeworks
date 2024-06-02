from turtle import *

speed(200)
width(5)

# to start things off, lets draw the main body of the castle
color("gray")
begin_fill()
penup()
goto(-100, -50)
pendown()

forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)

end_fill()

# now we have to draw the left tower
penup()
goto(-150, -50)
pendown()
begin_fill()

forward(50)
left(90)
forward(150)
left(90)
forward(50)
left(90)
forward(150)
left(90)

end_fill()

# draw the right tower
penup()
goto(100, -50)
pendown()
begin_fill()

forward(50)
left(90)
forward(150)
left(90)
forward(50)
left(90)
forward(150)
left(90)

end_fill()

# lets draw the fortifications on the main body
penup()
goto(-100, 50)
pendown()

begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
end_fill()

penup()
forward(40)
pendown()

begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
end_fill()

penup()
forward(40)
pendown()

begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
end_fill()

penup()
forward(40)
pendown()

begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
end_fill()

penup()
forward(40)
pendown()

begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
end_fill()

# done on the fortification, now lets draw the gate
penup()
goto(-30, -50)
pendown()
color("brown")
begin_fill()

forward(60)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)
left(90)

end_fill()

# alright, now draw the left window
penup()
goto(-70, 0)
pendown()
color("white")
begin_fill()

forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)

end_fill()

# lets draw the right window
penup()
goto(40, 0)
pendown()
begin_fill()

forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
end_fill()


# now its time to draw flag
# first lets draw the rod of flag
width(1)
color("black")

penup()
goto(100, 200)
pendown()
right(90)
forward(100)

# now lets draw the flag
color("red")

# move pen to the coordinates

penup()
goto(100,200)
pendown()

# now lets start drawing

begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()


# castle is built.



exitonclick()
