import turtle

# Create a turtle screen and turtle object
window = turtle.Screen()
t = turtle.Turtle()

# Set the turtle's speed (1 = slowest, 10 = fastest)
t.speed(2)

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Close the turtle graphics window when clicked
window.exitonclick()
