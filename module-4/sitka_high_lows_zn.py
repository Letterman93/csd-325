# ---------------------------------------------------------------
# Author:       Zak Nizam
# Date:         01/18/2026
# Course:       CSD325 - Advanced Python
# Assignment:   Module 4.2 – High/Low Temperatures
#
# Purpose:
#   This program reads weather data from a CSV file and allows the
#   user to display a graph of either daily high temperatures or
#   daily low temperatures for Sitka, Alaska (2018).
#
# Requirements Implemented:
#   - Show instructions/menu when the program starts.
#   - Allow the user to choose: Highs, Lows, or Exit.
#   - Graph highs in red and lows in blue.
#   - Loop until the user selects Exit.
#   - Provide an exit message when leaving the program.
#
# Files Needed:
#   - sitka_weather_2018_simple.csv
# ---------------------------------------------------------------

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


def load_weather_data(filename):
    """
    Read the CSV weather file and return lists of dates, highs, and lows.

    Returns:
        dates (list of datetime)
        highs (list of int)
        lows  (list of int)
    """
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # Skip header row.

        for row in reader:
            # Convert date string to a datetime object.
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)

            # Read high and low temperatures (TMAX and TMIN).
            high = int(row[5])
            low = int(row[6])

            highs.append(high)
            lows.append(low)

    return dates, highs, lows


def plot_temperatures(dates, temps, color, title, y_label):
    """
    Display a temperature graph.

    Parameters:
        dates (list of datetime): x-axis dates
        temps (list of int): temperature values
        color (str): line color (ex: 'red' or 'blue')
        title (str): chart title
        y_label (str): y-axis label
    """
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(y_label, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def display_menu():
    """
    Display program instructions/menu.
    """
    print("\nSitka Weather Viewer (2018)")
    print("Type one of the following options:")
    print("  highs - show the daily high temperatures")
    print("  lows  - show the daily low temperatures")
    print("  exit  - quit the program")


def main():
    """
    Main program loop:
    - Load the weather data once.
    - Repeatedly ask the user what they want to view.
    - Show highs (red) or lows (blue) until they choose exit.
    """
    filename = 'sitka_weather_2018_simple.csv'

    # Load data once so we don't reread the file each time.
    dates, highs, lows = load_weather_data(filename)

    # Program loop (runs until user exits).
    while True:
        display_menu()
        choice = input("zn: ").strip().lower()

        if choice == "highs":
            plot_temperatures(
                dates,
                highs,
                "red",
                "Daily high temperatures - 2018",
                "Temperature (F)"
            )

        elif choice == "lows":
            plot_temperatures(
                dates,
                lows,
                "blue",
                "Daily low temperatures - 2018",
                "Temperature (F)"
            )

        elif choice == "exit":
            print("Goodbye! Thanks for using the Sitka Weather Viewer.")
            sys.exit()

        else:
            print("Invalid option. Please type: highs, lows, or exit.")


if __name__ == "__main__":
    main()