import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def main():
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(2)
    
    side_length = 150  # You can adjust this value as needed
    draw_square(side_length)
    
    window.exitonclick()

if __name__ == "__main__":
    main()
