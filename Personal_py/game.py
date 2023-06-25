import curses

def main(stdscr):
    # Initialize curses
    stdscr.clear()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Make getch() non-blocking
    stdscr.timeout(100)  # Set refresh rate to 100 milliseconds

    # Initial character position
    character_x = 0
    character_y = 0

    # Game loop
    while True:
        # Get user input
        key = stdscr.getch()

        # Quit the game if 'q' is pressed
        if key == ord('q'):
            break

        # Move character based on arrow key input
        if key == curses.KEY_UP:
            character_y -= 1
        elif key == curses.KEY_DOWN:
            character_y += 1
        elif key == curses.KEY_LEFT:
            character_x -= 1
        elif key == curses.KEY_RIGHT:
            character_x += 1

        # Clear the screen
        stdscr.clear()

        # Draw the character at its new position
        stdscr.addch(character_y, character_x, '@')

        # Refresh the screen
        stdscr.refresh()

# Run the game
if __name__ == '__main__':
    curses.wrapper(main)
