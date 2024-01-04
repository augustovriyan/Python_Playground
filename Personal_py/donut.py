import math
import sys
import select
import time

# Constants for donut dimensions and screen size
A, B = 1, 1
WIDTH, HEIGHT = 80, 24

# Constants for animation speed and step sizes
THETA_STEP, PHI_STEP = 6, 2
A_STEP, B_STEP = 0.04, 0.02

# Colors for the donut
COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
COLOR_INDEX = 0

# Initialize the z-buffer
ZBUFFER = [[0] * WIDTH for _ in range(HEIGHT)]

def handle_user_input():
    """Handle user input for modifying donut properties."""
    if select.select([sys.stdin,],[],[],0.0)[0]:
        key = sys.stdin.readline().strip()
        
        global A_STEP, B_STEP, COLOR_INDEX
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
            COLOR_INDEX = (COLOR_INDEX + 1) % len(COLORS)

def render_donut():
    """Render the donut based on the current angles and properties."""
    output = ""
    cos_A, sin_A = math.cos(A), math.sin(A)
    cos_B, sin_B = math.cos(B), math.sin(B)

    for theta in range(0, 628, THETA_STEP):
        costheta, sintheta = math.cos(theta / 100), math.sin(theta / 100)

        for phi in range(0, 628, PHI_STEP):
            cosphi, sinphi = math.cos(phi / 100), math.sin(phi / 100)

            circle_x = cosphi
            circle_y = 2 + sinphi * costheta
            circle_z = 7 + sinphi * sintheta

            x = circle_x * cos_B + circle_y * sin_A * sin_B - circle_z * cos_A * sin_B
            y = circle_y * cos_A + circle_z * sin_A
            z = circle_x * sin_B - circle_y * sin_A * cos_B - circle_z * cos_A * cos_B
            ooz = 1 / z

            xp = int(WIDTH / 2 + x * ooz * WIDTH / 8)
            yp = int(HEIGHT / 2 - y * ooz * HEIGHT / 8)

            if 0 <= xp < WIDTH and 0 <= yp < HEIGHT:
                luminance_index = int((cosphi * costheta * sin_B - cos_A * costheta * sinphi -
                                       sin_A * sintheta + cosphi * sin_A * sintheta) * 8)

                if ooz > ZBUFFER[yp][xp]:
                    ZBUFFER[yp][xp] = ooz
                    output += COLORS[COLOR_INDEX] + ".,-~:;=!*#$@"[luminance_index] + "\033[0m"
                else:
                    output += " "
        output += "\n"

    sys.stdout.write("\033[2J\033[H" + output)
    sys.stdout.flush()

if __name__ == "__main__":
    while True:
        render_donut()
        A += A_STEP
        B += B_STEP
        handle_user_input()
        time.sleep(0.05)
