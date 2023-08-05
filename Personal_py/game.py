import curses
import random

def main(stdscr):
    # Initialize curses
    stdscr.clear()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Make getch() non-blocking
    stdscr.timeout(100)  # Set refresh rate to 100 milliseconds

    # Initialize game variables
    character_x = 0
    character_y = 0
    max_y, max_x = stdscr.getmaxyx()

    # Define boundaries
    boundary_top = 0
    boundary_bottom = max_y - 1
    boundary_left = 0
    boundary_right = max_x - 1

    # Define obstacles
    obstacles = []

    # Initialize score
    score = 0

    # Game loop
    while True:
        # Get user input
        key = stdscr.getch()

        # Quit the game if 'q' is pressed
        if key == ord('q'):
            break

        # Move character based on arrow key input
        if key == curses.KEY_UP and character_y > boundary_top:
            character_y -= 1
        elif key == curses.KEY_DOWN and character_y < boundary_bottom:
            character_y += 1
        elif key == curses.KEY_LEFT and character_x > boundary_left:
            character_x -= 1
        elif key == curses.KEY_RIGHT and character_x < boundary_right:
            character_x += 1

        # Check for collision with obstacles
        if (character_y, character_x) in obstacles:
            stdscr.addstr(max_y // 2, max_x // 2 - 5, "Game Over")
            stdscr.refresh()
            stdscr.getch()  # Wait for user input
            break

        # Increase the score if character passes an obstacle
        if character_y == boundary_top:
            score += 1

        # Clear the screen
        stdscr.clear()

        # Draw the character at its new position
        stdscr.addch(character_y, character_x, '@')

        # Draw the obstacles
        for obstacle in obstacles:
            stdscr.addch(obstacle[0], obstacle[1], '#')

        # Generate new obstacles randomly
        if random.random() < 0.1:  # Adjust the probability as needed
            obstacle_y = random.randint(boundary_top + 1, boundary_bottom - 1)
            obstacle_x = random.randint(boundary_left + 1, boundary_right - 1)
            obstacles.append((obstacle_y, obstacle_x))

        # Display the score
        stdscr.addstr(0, max_x - 10, f"Score: {score}")

        # Refresh the screen
        stdscr.refresh()

# Run the game
if __name__ == '__main__':
    curses.wrapper(main)
