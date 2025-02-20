# Dental Lab File Management System

## Overview
The **Dental Lab File Management System** is a Python-based desktop application designed to streamline file management workflows in dental labs. It offers a user-friendly GUI for monitoring directories, searching for cases, managing STL files, extracting ZIP files, and identifying missing case files. This tool is ideal for dental labs looking to improve efficiency and accuracy in handling digital case files.

---

![image](https://github.com/user-attachments/assets/d9a29108-1449-4953-ac04-244a14a16443)

## Features

### 1. Directory Monitoring
- Automatically detects file creation, modification, and deletion in a specified directory.
- Real-time updates displayed in the GUI.

### 2. Case Search
- Search for specific case folders or files using keywords or case numbers.
- Displays search results with file paths for easy navigation.

### 3. File Operations
- **Copy All Files**: Copy all files from the source directory to a target directory.
- **Copy STL Files**: Copy only STL files to a target directory.
- **Rename STL Files**: Rename STL files with optional structural modifications.
- **Rename Structure**: Apply specific naming conventions to STL files.

### 4. ZIP File Extraction
- Extract ZIP files from the source directory to a target location with one click.

### 5. Case Checker
- Input a list of case numbers to identify missing cases in the source directory.
- Displays missing cases in a dedicated section of the GUI.

### 6. Clear Missing Cases
- Reset the missing cases display with a single click.

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


