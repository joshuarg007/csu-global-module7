#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: course_lookup.py
Author: Joshua R. Gutierrez
Date: November 28, 2025
Version: 1.0
Description: Program that stores course information including room numbers,
instructors, and meeting times. The user enters a course number and the program
displays the corresponding room, instructor, and meeting time.
"""

def main():

# Dictionary of course numbers to room numbers
    course_rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    # Dictionary of course numbers to instructors
    course_instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    # Dictionary of course numbers to meeting times
    course_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    while True:
        # Ask the user for a course number
        course = input("Enter a course number (for example CSC101): ").strip().upper()

        if course == "EXIT":
            print("Goodbye.")
            break
        
        # Look up the course information
        if course in course_rooms:
            print(f"Course: {course}")
            print(f"Room number: {course_rooms[course]}")
            print(f"Instructor: {course_instructors[course]}")
            print(f"Meeting time: {course_times[course]}")
        else:
            print("That course number was not found.")


if __name__ == "__main__":
    main()
