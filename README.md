# Dental Lab File Management System

The Dental Lab File Management System is a Python-based application designed to assist dental labs in managing case files, STL files, and ZIP archives. It offers features like case checking, file copying, renaming, ZIP extraction, and real-time file monitoring.

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

---

### GUI Overview
The GUI includes the following functionalities:

1. **Source Directory Selection**:
   - Select the directory containing case files or STL files.

2. **Case Checker**:
   - Enter case numbers to check for missing cases in the selected directory.

3. **File Operations**:
   - Copy all folders.
   - Copy STL files only.
   - Rename STL files with `_copy` suffix.
   - Rename STL files and maintain folder structures.

4. **ZIP Extraction**:
   - Extract ZIP files from the source directory to a target directory.

5. **File Monitoring**:
   - Monitor a specified directory for file events (creation, modification, deletion).

## Features

- **Case Checker**: Identify missing case numbers from a specified directory.
- **STL File Management**: Copy and rename STL files while preserving folder structures.
- **ZIP Extraction**: Extract ZIP files into organized directories.
- **File Monitoring**: Monitor a directory for file creation, modification, or deletion events.
- **GUI Interface**: User-friendly interface for seamless interaction with all features.

## Installation

Clone the repository and install the required dependencies using `pip`.

git clone <repository_url>
cd dental-lab-file-management
pip install -r requirements.txt



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


