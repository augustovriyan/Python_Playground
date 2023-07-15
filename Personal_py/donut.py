import math
import time

# Dimensions of the donut and the screen
A = 1
B = 1
width = 80
height = 24

# Animation loop
while True:
    output = ""
    zbuffer = [[0] * width for _ in range(height)]

    cos_A = math.cos(A)
    sin_A = math.sin(A)
    cos_B = math.cos(B)
    sin_B = math.sin(B)

    for theta in range(0, 628, 6):
        costheta = math.cos(theta / 100)
        sintheta = math.sin(theta / 100)

        for phi in range(0, 628, 2):
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
                    output += ".,-~:;=!*#$@"[luminance_index]

        output += "\n"

    # Clear the console and display the donut
    print("\033[2J\033[H" + output)

    # Update the angles for spinning effect
    A += 0.04
    B += 0.02

    # Pause briefly to control the animation speed
    time.sleep(0.05)