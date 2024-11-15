'''
<summary>
This is the main entry point for the application. It handles user input and orchestrates the various operations.
</summary>
<copyright file="main.py" company="Nakanishi Dental Lab, Inc.">
Copyright (c) Nakanishi Dental Lab, Inc. All rights reserved. 11/8/2024
</copyright>
'''

import logging
import os
import time
from watchdog.observers import Observer
from folder_manager import FolderManager
from folder_search import FolderSearcher
from input_handler import InputHandler
from copy_stl import STLFileHandler
from checking_missing_cases import CaseChecker
from extract_zip import ZipExtractor
from file_monitoring import FileHandler

def monitor_directory(path, log_file):
    event_handler = FileHandler(log_file)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    return observer

def main():
    # Set up logging
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, 'file_tracking.log')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    input_handler = InputHandler()
    folder_searcher = FolderSearcher()
    folder_manager = FolderManager()
    zip_extractor = ZipExtractor()
    stl_handler = STLFileHandler()
    case_checker = CaseChecker()

    print("Welcome to the Nakanishi Dental Lab File Management System!")
    
    # Start monitoring the directory
    directory_to_watch = r"\\NAKA-APP03\3Shape Dental System Orders\ManufacturingDir"
    observer = monitor_directory(directory_to_watch, log_file)
    print(f"Started monitoring directory: {directory_to_watch}")
    print(f"File tracking log will be saved to: {log_file}")

    try:
        source_directory = input_handler.get_source_directory()
        while True:
            try:
                choice = input_handler.get_user_choice()

                if choice == '1':
                    case_numbers = input_handler.get_case_numbers()
                    found_folders = folder_searcher.search_by_case_numbers(source_directory, case_numbers)
                    case_checker.find_missing_cases(source_directory, case_numbers)
                elif choice == '2':
                    search_terms = input_handler.get_search_terms()
                    found_folders = folder_searcher.search_by_name(source_directory, search_terms)
                elif choice == '3':
                    query = input_handler.get_search_query()
                    found_folders = folder_searcher.pan_search(source_directory, query)
                elif choice == '4':
                    folder_manager.list_all_folders(source_directory)
                    continue
                elif choice == '5':
                    zip_files = folder_manager.list_zip_files(source_directory)
                    if zip_files:
                        target_directory = input_handler.get_target_directory()
                        for zip_file in zip_files:
                            zip_extractor.extract_zip_file(os.path.join(source_directory, zip_file), target_directory)
                    continue
                elif choice == '6':
                    case_numbers = input_handler.get_case_numbers()
                    case_checker.find_missing_cases(source_directory, case_numbers)
                    continue
                else:
                    print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
                    continue

                if found_folders:
                    print("\nFound folders/files:")
                    for name, path in found_folders.items():
                        print(f"{name}: {path}")

                    target_directory = input_handler.get_target_directory()
                    action_choice = input_handler.get_action_choice()

                    if action_choice == '1':
                        folder_manager.copy_contents(target_directory, found_folders)
                    elif action_choice == '2':
                        stl_handler.copy_stl_files(list(found_folders.values()), target_directory)
                    elif action_choice == '3':
                        stl_handler.copy_stl_files(list(found_folders.values()), target_directory, rename=True)
                    elif action_choice == '4':
                        stl_handler.rename_stl_files_with_structure(list(found_folders.values()), target_directory)
                    else:
                        print("Invalid choice. Please enter 1, 2, 3, or 4.")
                else:
                    print("No folders found based on your search criteria.")

            except Exception as e:
                logging.error(f"An error occurred: {str(e)}")
                print(f"An error occurred: {str(e)}")

            if not input("\nWould you like to perform another search in the same directory? (y/n): ").lower().startswith('y'):
                if not input("Would you like to change the source directory? (y/n): ").lower().startswith('y'):
                    print("Thank you for using the Nakanishi Dental Lab File Management System. Goodbye!")
                    break
                else:
                    source_directory = input_handler.get_source_directory()

    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()