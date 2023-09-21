import turtle

# Create a turtle screen and turtle object
window = turtle.Screen()
t = turtle.Turtle()

# Set the turtle's speed (1 = slowest, 10 = fastest)
t.speed(2)

# Define the side length of the square
side_length = 150  # You can adjust this value as needed

# Draw a square
for _ in range(4):
    t.forward(side_length)  # Move forward by the specified side length
    t.right(90)             # Turn right by 90 degrees

# Close the turtle graphics window when clicked
window.exitonclick()
