# Dental Lab File Management System

## Overview
The **Dental Lab File Management System** is a Python-based desktop application designed to streamline file management workflows in dental labs. It offers a user-friendly GUI for monitoring directories, searching for cases, managing STL files, extracting ZIP files, and identifying missing case files. This tool is ideal for dental labs looking to improve efficiency and accuracy in handling digital case files.

---

![image](https://github.com/user-attachments/assets/d9a29108-1449-4953-ac04-244a14a16443)
The intuitive GUI includes:
- Source directory selection.
- Search functionality with results display.
- Action buttons for file operations.
- Case checker for identifying missing cases.
- Real-time file monitoring status.

---

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

---

## How It Works

### Directory Monitoring
The application uses the [Watchdog](https://pypi.org/project/watchdog/) library to monitor file events (creation, modification, deletion) in real time. Events are logged and displayed in the GUI.

### GUI Components
The application is built using [PyQt5](https://pypi.org/project/PyQt5/) and includes:
1. **Source Directory Selection**: Choose the folder to monitor or perform actions on.
2. **Search Input**: Enter keywords or case numbers to find specific folders/files.
3. **Results Display**: View search results or missing cases in real-time.
4. **Action Buttons**:
   - Copy all files or only STL files.
   - Rename STL files with or without structural modifications.
5. **Case Checker**: Identify missing case numbers from a provided list.

---

## Usage

### Step-by-Step Instructions

#### 1. Select Source Directory
Click the "Select Source Directory" button and choose the folder you want to monitor or work with.

#### 2. Search for Cases
Enter case numbers or keywords in the search bar and click "Search." The results will be displayed in the text area below.

#### 3. Perform File Operations
Use the action buttons to:
- Copy all files or only STL files to a target directory.
- Rename STL files based on your preferences.

#### 4. Extract ZIP Files
Click "Extract ZIP" to extract all ZIP files from the source directory into a target folder.

#### 5. Check for Missing Cases
Input a list of case numbers (comma-separated) into the "Case Checker" section and click "Check Cases." Missing cases will be displayed below.

#### 6. Monitor Files in Real-Time
The application automatically monitors changes (creation, modification, deletion) in the specified directory and displays updates in real-time.

---

## Code Structure

The project is modularized into several components:

| Module                  | Description                                      |
|-------------------------|--------------------------------------------------|
| `folder_manager.py`     | Handles folder operations like copying contents. |
| `folder_search.py`      | Implements search functionality by keywords/cases.|
| `copy_stl.py`           | Manages STL file-specific operations like renaming or copying. |
| `checking_missing_cases.py` | Identifies missing cases based on input criteria. |
| `extract_zip.py`        | Extracts ZIP files from source to target directories. |
| `file_monitoring.py`    | Monitors real-time file events using Watchdog.   |

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a feature branch:


## License

This project is licensed under the MIT License

## Acknowledgments

- PyQt5 for the GUI framework
- watchdog for file system monitoring


