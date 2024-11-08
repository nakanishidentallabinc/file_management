# Nakanishi Dental Lab File Management System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Copyright](#copyright)

## Overview

The Nakanishi Dental Lab File Management System is a light tool designed to search and manage dental case files and STL files. It provides functionalities for searching, copying, and organizing files, streamlining the workflow for dental lab professionals.

## Features

### Search Functionality
- Search by case numbers
- Search by last name
- Pan search for folders
- List all folders in a directory
- List all ZIP files in a directory

### File Operations
- Copy entire folders with all files
- Copy only STL files
- Copy and rename STL files (adding '_copy' suffix)
- Copy and rename STL files and folders while maintaining structure

### Case Management
- Check for missing cases
- Extract ZIP files

### User Interface
- Interactive command-line interface
- User-friendly prompts for input

## Project Structure

The project is organized into several Python modules:

- `main.py`: Main entry point of the application
- `folder_manager.py`: Manages folder operations
- `folder_search.py`: Handles folder search operations
- `input_handler.py`: Manages user input
- `copy_stl.py`: Handles STL file operations
- `checking_missing_cases.py`: Checks for missing case files
- `extract_zip.py`: Extracts ZIP files

## Installation

1. Clone the repository:

  git clone https://github.com/nakanishi-dental-lab/file-management-system.git

3. Navigate to the project directory:

  cd file-management

## Usage

1. Run the main script:

   python3 main.py

3. Follow the on-screen prompts to perform various operations.
4. Choose from the available options to search, copy, or manage files.

## Requirements

- Python 3.x
- No additional libraries required (uses standard library modules)

## Copyright

Copyright © 2024 Nakanishi Dental Lab, Inc. All rights reserved.

---

For more detailed information about each module and its functions, please refer to the individual Python files and their docstrings.
