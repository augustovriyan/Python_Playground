import curses
import random

# Constants
OBSTACLE_PROBABILITY = 0.1

def handle_user_input(character_y, character_x, boundaries):
    """Handle user input to move the character."""
    key = stdscr.getch()

    if key == ord('q'):
        return True  # Quit the game

    # Update character position based on arrow key input
    if key == curses.KEY_UP and character_y > boundaries[0]:
        character_y -= 1
    elif key == curses.KEY_DOWN and character_y < boundaries[1]:
        character_y += 1
    elif key == curses.KEY_LEFT and character_x > boundaries[2]:
        character_x -= 1
    elif key == curses.KEY_RIGHT and character_x < boundaries[3]:
        character_x += 1

    return False

def generate_obstacle(boundaries):
    """Generate a random obstacle within the specified boundaries."""
    obstacle_y = random.randint(boundaries[0] + 1, boundaries[1] - 1)
    obstacle_x = random.randint(boundaries[2] + 1, boundaries[3] - 1)
    return (obstacle_y, obstacle_x)

def main(stdscr):
    """Main game loop."""
    stdscr.clear()
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Set timeout for getch()

    # Initialize character position and game boundaries
    character_x, character_y = 0, 0
    max_y, max_x = stdscr.getmaxyx()
    boundaries = (0, max_y - 1, 0, max_x - 1)

    obstacles = []
    score = 0

    while True:
        if handle_user_input(character_y, character_x, boundaries):
            break

        # Check for collision with obstacles
        if (character_y, character_x) in obstacles:
            stdscr.addstr(max_y // 2, max_x // 2 - 5, "Game Over")
            stdscr.refresh()
            stdscr.getch()
            break

        # Increase score when character reaches the top boundary
        if character_y == boundaries[0]:
            score += 1

        # Clear the screen and update the game elements
        stdscr.clear()
        stdscr.addch(character_y, character_x, '@')  # Draw character

        for obstacle in obstacles:
            stdscr.addch(obstacle[0], obstacle[1], '#')  # Draw obstacles

        # Randomly generate obstacles
        if random.random() < OBSTACLE_PROBABILITY:
            obstacles.append(generate_obstacle(boundaries))

        # Display score on the screen
        stdscr.addstr(0, max_x - 10, f"Score: {score}")
        stdscr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
