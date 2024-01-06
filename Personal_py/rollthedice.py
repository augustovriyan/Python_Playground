import random
import matplotlib.pyplot as plt
from collections import Counter

def roll_dice(num_dice, num_sides):
    """Simulate rolling 'num_dice' with 'num_sides' and return the rolls and frequencies."""
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls, Counter(rolls)

def get_positive_integer_input(prompt):
    """Prompt the user for a positive integer input."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Value must be a positive integer.")
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def plot_bar_chart(data, title, xlabel, ylabel):
    """Plot a bar chart based on the given data."""
    x_values, y_values = zip(*data.items())
    plt.bar(x_values, y_values, color='skyblue', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()

def plot_cumulative_chart(data, title, xlabel, ylabel):
    """Plot a cumulative frequency chart based on the given data."""
    x_values, y_values = zip(*data.items())
    cumulative_freq = [sum(y_values[:i + 1]) for i in range(len(y_values))]
    
    plt.figure()
    plt.plot(x_values, cumulative_freq, marker='o', linestyle='-', color='green')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()

def main():
    """Main function to simulate dice rolling and plot frequencies."""
    num_dice = get_positive_integer_input("Enter the number of dice to roll: ")
    num_sides = get_positive_integer_input("Enter the number of sides on each die: ")

    rolls, frequencies = roll_dice(num_dice, num_sides)
    total_sum = sum(rolls)

    print(f"Rolling {num_dice} dice with {num_sides} sides each...")
    print(f"Results: {rolls}")
    print(f"Total: {total_sum}")
    print(f"Frequencies: {dict(frequencies)}")

    plot_bar_chart(frequencies, 'Dice Roll Frequencies', 'Dice Roll', 'Frequency')
    plot_cumulative_chart(frequencies, 'Cumulative Dice Roll Frequencies', 'Dice Roll', 'Cumulative Frequency')
    
    plt.show()

    repeat = input("Do you want to roll the dice again? (yes/no): ").lower()
    if repeat == "yes":
        main()

if __name__ == "__main__":
    main()
