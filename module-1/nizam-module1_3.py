# ---------------------------------------------------------------
# Author:       Zak Nizam
# Date:         January 2026
# Course:       CSD325 - Advanced Python
# Assignment:   Module 1 – On the Wall
#
# Purpose:
#   Ask the user for a starting number of bottles and then display
#   the "bottles of beer on the wall" countdown song until there
#   are no bottles left, followed by a reminder to buy more.
# ---------------------------------------------------------------

def countdown(bottles):
    """
    Flowchart: Countdown function
    - Loop while there are bottles remaining.
    - Print the correct verse for plural or singular bottles.
    - Decrease the bottle count by one each time.
    """
    # Flowchart: Loop while BOTTLES > 0
    while bottles > 0:
        # Flowchart: Decision – is BOTTLES equal to 1?
        if bottles == 1:
            # Flowchart: Print singular verse
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        else:
            # Flowchart: Print plural verse
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        # Flowchart: Calculate next bottle count (BOTTLES - 1)
        next_bottles = bottles - 1

        # Flowchart: Print "Take one down..." line with next count
        print(f"Take one down and pass it around, {next_bottles} bottle(s) of beer on the wall.\n")

        # Flowchart: Update BOTTLES with the new value
        bottles = next_bottles


def main():
    """
    Flowchart: Main program
    - Start program.
    - Ask user for number of bottles and store in BOTTLES.
    - Call countdown(BOTTLES).
    - Print final reminder to buy more bottles.
    - End program.
    """
    # Flowchart: Ask for starting number of bottles
    starting_bottles = int(input("Enter number of bottles:"))

    # Flowchart: Call countdown function with BOTTLES
    countdown(starting_bottles)

    # Flowchart: Final message after countdown is finished
    print("Time to buy more bottles of beer.\n")


# Flowchart: Program entry point (START / END)
if __name__ == "__main__":
    main()