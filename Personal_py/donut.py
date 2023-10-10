import math
import time
import sys
import select

# Constants for donut dimensions and screen size
A = 1
B = 1
width = 80
height = 24

# Constants for animation speed and step sizes
THETA_STEP = 6
PHI_STEP = 2
A_STEP = 0.04
B_STEP = 0.02

# Colors for the donut
colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
color_index = 0

# Initialize the z-buffer
zbuffer = [[0] * width for _ in range(height)]

# Function to handle user input
def handle_user_input():
    if select.select([sys.stdin,],[],[],0.0)[0]:
        key = sys.stdin.readline().strip()
        global A_STEP, B_STEP, color_index

        if key == 'q':
            sys.exit(0)
        elif key == 'f':
            A_STEP += 0.01
        elif key == 's':
            A_STEP -= 0.01
        elif key == 'r':
            B_STEP += 0.01
        elif key == 'l':
            B_STEP -= 0.01
        elif key == 'c':
            color_index = (color_index + 1) % len(colors)

# Function to render the donut
def render_donut():
    output = ""

    cos_A = math.cos(A)
    sin_A = math.sin(A)
    cos_B = math.cos(B)
    sin_B = math.sin(B)

    for theta in range(0, 628, THETA_STEP):
        costheta = math.cos(theta / 100)
        sintheta = math.sin(theta / 100)

        for phi in range(0, 628, PHI_STEP):
            cosphi = math.cos(phi / 100)
            sinphi = math.sin(phi / 100)

            circle_x = cosphi
            circle_y = 2 + sinphi * costheta
            circle_z = 7 + sinphi * sintheta

            # 3D to 2D projection
            x = circle_x * cos_B + circle_y * sin_A * sin_B - circle_z * cos_A * sin_B
            y = circle_y * cos_A + circle_z * sin_A
            z = circle_x * sin_B - circle_y * sin_A * cos_B - circle_z * cos_A * cos_B
            ooz = 1 / z

            xp = int(width / 2 + x * ooz * width / 8)
            yp = int(height / 2 - y * ooz * height / 8)

            if 0 <= xp < width and 0 <= yp < height:
                luminance_index = int((cosphi * costheta * sin_B - cos_A * costheta * sinphi -
                                       sin_A * sintheta + cosphi * sin_A * sintheta) * 8)

                if ooz > zbuffer[yp][xp]:
                    zbuffer[yp][xp] = ooz

                    # Add color to the donut
                    color = colors[color_index]
                    output += color + ".,-~:;=!*#$@"[luminance_index] + "\033[0m"

                else:
                    output += " "
        output += "\n"

    # Clear the console and display the donut
    sys.stdout.write("\033[2J\033[H" + output)
    sys.stdout.flush()

# Animation loop
while True:
    # Render the donut
    render_donut()

    # Update the angles for spinning effect
    A += A_STEP
    B += B_STEP

    # Handle user input
    handle_user_input()

    # Pause briefly to control the animation speed
    time.sleep(0.05)
