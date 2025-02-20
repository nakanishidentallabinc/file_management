# Nakanishi Dental Lab File Management System

This application is a comprehensive file management system designed for Nakanishi Dental Lab, Inc. It provides various functionalities to manage dental case files, including searching, copying, renaming, and monitoring file operations.

## Features

- **File Search**: Search for case files using case numbers, names, or custom queries.
- **File Operations**: Copy, rename, and manage STL files and folder structures.
- **Case Checking**: Identify missing cases from a list of case numbers.
- **ZIP Extraction**: Extract ZIP files found in the source directory.
- **File Monitoring**: Monitor a specified directory for file changes (creation, modification, deletion).
- **File Statistics**: View file operation counts for a specific date.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/nakanishidentallabinc/file_management.git
   ```

2. Install the required dependencies:
   ```
   pip install PyQt5 watchdog
   ```

## Usage

Run the main script to start the application:

```
python main.py
```

The application will launch a graphical user interface (GUI) with the following main features:

- Select source and target directories
- Search for files and folders
- Perform various file operations (copy, rename)
- Check for missing cases
- Extract ZIP files
- Monitor file changes in a specified directory

## File Structure

- `main.py`: The main entry point of the application, containing the GUI implementation.
- `folder_manager.py`: Handles folder operations like copying and listing.
- `folder_search.py`: Implements file and folder search functionality.
- `input_handler.py`: Manages user input for various operations.
- `copy_stl.py`: Handles STL file operations.
- `checking_missing_cases.py`: Implements case checking functionality.
- `extract_zip.py`: Manages ZIP file extraction.
- `file_monitoring.py`: Implements file monitoring using watchdog.


## License

This project is licensed under the MIT License

## Acknowledgments

- PyQt5 for the GUI framework
- watchdog for file system monitoring


![image](https://github.com/user-attachments/assets/d9a29108-1449-4953-ac04-244a14a16443)


