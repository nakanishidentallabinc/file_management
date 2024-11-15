'''
<summary>
This module contains functions for handling user input for directory paths and case numbers.
</summary>
<copyright file="input_handler.py" company="Nakanishi Dental Lab, Inc.">
Copyright (c) Nakanishi Dental Lab, Inc. All rights reserved. 11/8/2024
</copyright>
'''


import os

class InputHandler:
    def get_source_directory(self):
        while True:
            source_directory = input("Enter the source directory path: ")
            if os.path.isdir(source_directory):
                return source_directory
            print("The specified source directory does not exist. Please try again.")

    def get_case_numbers(self):
        while True:
            user_input = input("Enter the case numbers to search for (separated by commas): ")
            case_numbers = [case.strip() for case in user_input.split(',') if case.strip()]
            if case_numbers:
                return case_numbers
            print("No valid case numbers entered. Please try again.")

    def get_target_directory(self):
        target_directory = input("Enter the temporary directory where you want to create these folders: ")
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
            print(f"Temporary directory created at: {target_directory}")
        return target_directory

    def get_user_choice(self):
        print("\nPlease select an option:")
        print("1. Search by case numbers")
        print("2. Search by name")
        print("3. Pan search")
        print("4. List all folders")
        print("5. Extract ZIP files")
        print("6. Check for missing cases")
        print("7. View file counts for a specific day")
        return input("Enter your choice (1-7): ")


    def get_search_terms(self):
        search_terms_input = input("Enter the names or substrings to search for (separated by commas): ")
        return [term.strip() for term in search_terms_input.split(',')]

    def get_search_query(self):
        return input("Enter the substring to search for: ")

    def get_action_choice(self):
        print("\nWhat would you like to do?")
        print("1. Copy all folders with files")
        print("2. Copy only STL files")
        print("3. Copy and rename STL files (add '_copy')")
        print("4. Copy and rename STL files and folders (maintain structure)")
        return input("Enter your choice (1/2/3/4): ").strip()