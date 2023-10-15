import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)

# Function to draw a petal
def draw_petal():
    for _ in range(36):
        flower.color("red")
        flower.forward(100)
        flower.right(45)
        flower.forward(100)
        flower.right(135)
        flower.forward(100)
        flower.right(45)
        flower.forward(100)
        flower.right(170)
    flower.right(10)

# Draw the flower
flower.penup()
flower.goto(0, -200)
flower.pendown()
for _ in range(12):
    draw_petal()
    flower.right(30)

# Draw the stem
flower.color("green")
flower.penup()
flower.goto(0, -200)
flower.pendown()
flower.setheading(90)
flower.forward(200)

# Close the window on click
screen.exitonclick()
