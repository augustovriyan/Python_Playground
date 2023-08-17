import random
import matplotlib.pyplot as plt
from collections import defaultdict

def roll_dice(num_dice, num_sides):
    rolls = []
    frequencies = defaultdict(int)  # Default value of 0 for missing keys

    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
        frequencies[roll] += 1

    return rolls, frequencies

def main():
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            num_sides = int(input("Enter the number of sides on each die: "))
            if num_dice <= 0 or num_sides <= 0:
                raise ValueError("Number of dice and sides must be positive integers.")
            break
        except ValueError as e:
            print("Invalid input:", e)

    rolls, frequencies = roll_dice(num_dice, num_sides)
    total = sum(rolls)

    print("Rolling {} dice with {} sides each...".format(num_dice, num_sides))
    print("Results: {}".format(rolls))
    print("Total: {}".format(total))
    print("Frequencies: {}".format(frequencies))

    # Plotting the histogram
    x = list(frequencies.keys())
    y = list(frequencies.values())

    plt.bar(x, y, color='skyblue', edgecolor='black')  # Custom colors and edge color
    plt.xlabel('Dice Roll')
    plt.ylabel('Frequency')
    plt.title('Dice Roll Frequencies')

    total_rolls = sum(y)
    for i, v in enumerate(y):
        percentage = (v / total_rolls) * 100
        plt.text(x[i], v + 0.1, f'{v} ({percentage:.2f}%)', ha='center', va='bottom', fontsize=10)

    plt.xticks(x)
    plt.grid(axis='y', alpha=0.75)

    plt.tight_layout()

    # Cumulative Frequency Plot
    cumulative_frequencies = [sum(y[:i + 1]) for i in range(len(y))]
    plt.figure()
    plt.plot(x, cumulative_frequencies, marker='o', linestyle='-', color='green')
    plt.xlabel('Dice Roll')
    plt.ylabel('Cumulative Frequency')
    plt.title('Cumulative Dice Roll Frequencies')
    plt.grid()

    plt.show()

    repeat = input("Do you want to roll the dice again? (yes/no): ")
    if repeat.lower() == "yes":
        main()

if __name__ == "__main__":
    main()
