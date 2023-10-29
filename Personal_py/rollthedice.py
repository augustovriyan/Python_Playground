import random
import matplotlib.pyplot as plt
from collections import Counter

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    frequencies = Counter(rolls)

    return rolls, frequencies

def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Value must be a positive integer.")
            return value
        except ValueError as e:
            print("Invalid input:", e)

def plot_histogram(frequencies):
    x, y = zip(*frequencies.items())

    plt.bar(x, y, color='skyblue', edgecolor='black')
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

def plot_cumulative_frequency(frequencies):
    x, y = zip(*frequencies.items())
    cumulative_frequencies = [sum(y[:i + 1]) for i in range(len(y))]

    plt.figure()
    plt.plot(x, cumulative_frequencies, marker='o', linestyle='-', color='green')
    plt.xlabel('Dice Roll')
    plt.ylabel('Cumulative Frequency')
    plt.title('Cumulative Dice Roll Frequencies')
    plt.grid()

def main():
    num_dice = get_positive_integer_input("Enter the number of dice to roll: ")
    num_sides = get_positive_integer_input("Enter the number of sides on each die: ")

    rolls, frequencies = roll_dice(num_dice, num_sides)
    total = sum(rolls)

    print(f"Rolling {num_dice} dice with {num_sides} sides each...")
    print(f"Results: {rolls}")
    print(f"Total: {total}")
    print(f"Frequencies: {dict(frequencies)}")

    plot_histogram(frequencies)
    plot_cumulative_frequency(frequencies)
    plt.show()

    repeat = input("Do you want to roll the dice again? (yes/no): ")
    if repeat.lower() == "yes":
        main()

if __name__ == "__main__":
    main()
