import random

def roll_dice(num_dice, num_sides):
    rolls = []
    frequencies = {}  # Dictionary to store the frequencies

    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)

        # Update the frequencies dictionary
        frequencies[roll] = frequencies.get(roll, 0) + 1

    return rolls, frequencies

def main():
    num_dice = int(input("Enter the number of dice to roll: "))
    num_sides = int(input("Enter the number of sides on each die: "))

    rolls, frequencies = roll_dice(num_dice, num_sides)
    total = sum(rolls)

    print("Rolling {} dice with {} sides each...".format(num_dice, num_sides))
    print("Results: {}".format(rolls))
    print("Total: {}".format(total))
    print("Frequencies: {}".format(frequencies))

if __name__ == "__main__":
    main()
