import curses

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
    obstacles = [(5, 10), (8, 20), (12, 5)]  # Example obstacle positions

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
            character_y = 0  # Reset character position if collision occurs

        # Clear the screen
        stdscr.clear()

        # Draw the character at its new position
        stdscr.addch(character_y, character_x, '@')

        # Draw the obstacles
        for obstacle in obstacles:
            stdscr.addch(obstacle[0], obstacle[1], '#')

        # Refresh the screen
        stdscr.refresh()

# Run the game
if __name__ == '__main__':
    curses.wrapper(main)
