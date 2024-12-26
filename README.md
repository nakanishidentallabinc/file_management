# Nakanishi Dental Lab File Management System

## Overview

The Nakanishi Dental Lab File Management System is a comprehensive tool designed to streamline file operations, case management, and monitoring for dental laboratories. This application provides an intuitive graphical user interface for efficient handling of dental case files, STL file management, and automated file monitoring.

## Features

- **File Search**: Easily search for folders and files within a specified source directory.
- **Case Checking**: Identify missing cases by comparing input case numbers against existing files.
- **File Operations**: Perform various actions such as copying all files, copying STL files, and renaming structures.
- **ZIP Extraction**: Extract ZIP files from a source directory to a target location.
- **File Monitoring**: Automatically track file changes in a specified directory.
- **User-Friendly Interface**: Intuitive GUI with clear sections for different functionalities.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required dependencies:
   ```
   pip install PyQt5 watchdog
   ```
3. Clone or download the repository to your local machine.

## Usage

1. Run the main script:
   ```
   python main.py
   ```
2. Use the interface to select source directories, perform searches, and execute file operations.
3. Monitor the status bar for file monitoring updates and operation results.

## Key Components

- **MainWindow**: The primary application window containing all UI elements and core functionality.
- **FolderSearcher**: Handles directory searches based on user input.
- **FolderManager**: Manages folder operations like copying contents.
- **STLFileHandler**: Specializes in STL file operations, including copying and renaming.
- **CaseChecker**: Verifies the presence of case files and reports missing cases.
- **ZipExtractor**: Manages the extraction of ZIP files.
- **FileMonitorThread**: Runs a background thread for continuous file monitoring.

## Contributing

Contributions to improve the Nakanishi Dental Lab File Management System are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

