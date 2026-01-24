# ---------------------------------------------------------------
# Author:       Zak Nizam
# Date:         12/08/2026
# Course:       CSD325 - Advanced Python
# Assignment:   Module 2 – Documented Debugging
#
# Purpose:
#   Use a simple selection structure to decide whether the user
#   should bring an umbrella before going outside.
#   This program matches the "Selection Flowchart":
#   Start -> Is it raining? -> Bring umbrella / Go outside -> End
# ---------------------------------------------------------------

def decide_umbrella(is_raining):
    """
    Decide whether the user should bring an umbrella.

    Parameters:
        is_raining (bool): True if it is raining, False otherwise.

    This function prints a message that matches the flowchart steps.
    """
    if is_raining:
        print("It is raining.")
        print("Bring an umbrella.")
    else:
        print("It is not raining.")
        print("You do not need an umbrella.")

    # In both cases, the last step is to go outside.
    print("Go outside.")

def main():
    """
    Main program:
    - Ask the user if it is raining.
    - Convert the answer to a True/False value.
    - Call decide_umbrella() with the result.
    """
    answer = input("Is it raining? (yes/no): ").strip().lower()

    # Treat 'yes' or 'y' as raining, everything else as not raining.
    is_raining = answer in ("yes", "y")

    decide_umbrella(is_raining)


if __name__ == "__main__":
    main()