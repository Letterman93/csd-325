# ---------------------------------------------------------------
# Author:       Zak Nizam
# Date:         02/12/2026
# Course:       CSD325 - Advanced Python
# Assignment:   Module 8.2 – JSON Practice
#
# Purpose:
#   Load a student list from Student.json, display it, add a new
#   student, display the updated list, then save it back to JSON.
# ---------------------------------------------------------------

import json


def print_student_list(student_list, message):
    """
    Print each student record in a readable format.

    Output format example:
    Ripley, Ellen : ID = 45604 , Email = eripley@gmail.com
    """
    print(message)

    for student in student_list:
        last_name = student["L_Name"]
        first_name = student["F_Name"]
        student_id = student["Student_ID"]
        email = student["Email"]

        print(f"{last_name}, {first_name} : ID = {student_id} , Email = {email}")

    print()  # blank line for spacing


def main():
    # Step 1: Load the JSON file into a Python list
    filename = "Student.json"

    with open(filename, "r", encoding="utf-8") as file:
        student_list = json.load(file)

    # Step 2: Print original list
    print_student_list(student_list, "Original Student list:")

    # Step 3: Add your new student record (append)
    new_student = {
        "F_Name": "Zak",
        "L_Name": "Nizam",
        "Student_ID": 90001,
        "Email": "znizam90001@gmail.com"
    }
    student_list.append(new_student)

    # Step 4: Print updated list
    print_student_list(student_list, "Updated Student list:")

    # Step 5: Save the updated list back to the JSON file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(student_list, file, indent=4)

    # Step 6: Notify user the file was updated
    print("The Student.json file was updated.")


if __name__ == "__main__":
    main()