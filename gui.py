import sys
import os
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog, QMessageBox,QGroupBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from watchdog.observers import Observer
from folder_manager import FolderManager
from folder_search import FolderSearcher
from input_handler import InputHandler
from copy_stl import STLFileHandler
from checking_missing_cases import CaseChecker
from extract_zip import ZipExtractor
from file_monitoring import FileHandler
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from extract_zip import ZipExtractor

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLineEdit, QTextEdit, 
                             QLabel, QFileDialog, QMessageBox, QInputDialog)

class FileMonitorThread(QThread):
    file_event = pyqtSignal(str)

    def __init__(self, directory, log_file):
        super().__init__()
        self.directory = directory
        self.log_file = log_file

    def run(self):
        event_handler = FileHandler(self.log_file)
        observer = Observer()
        observer.schedule(event_handler, self.directory, recursive=True)
        observer.start()
        try:
            while True:
                self.sleep(1)
        except:
            observer.stop()
        observer.join()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nakanishi Dental Lab File Management System")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        


        self.setup_ui()

        self.folder_searcher = FolderSearcher()
        self.folder_manager = FolderManager()
        self.zip_extractor = ZipExtractor()
        self.stl_handler = STLFileHandler()
        self.case_checker = CaseChecker()
        self.zip_extractor = ZipExtractor()

        self.source_directory = ""
        self.target_directory = ""

        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(script_dir, 'file_tracking.log')
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        self.start_file_monitoring()

        self.setup_case_checker_ui()

        # Apply some styling
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #cccccc;
                border-radius: 6px;
                margin-top: 6px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 7px;
                padding: 0px 5px 0px 5px;
            }
            QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 4px;
            }
            QPushButton {
                background-color: #0078D7;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #1084D9;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #cccccc;
                border-radius: 4px;
            }
        """)



    # ... (other existing methods) ...

    def perform_search(self):
        if not self.source_directory:
            QMessageBox.warning(self, "Error", "Please select a source directory first.")
            return

        search_terms = self.search_input.text().split(',')
        found_folders = self.folder_searcher.search_by_name(self.source_directory, search_terms)

        if found_folders:
            self.results_display.clear()
            self.results_display.append("Found folders/files:")
            for name, path in found_folders.items():
                self.results_display.append(f"{name}: {path}")
            
            # Check for missing cases
            case_numbers = [term.strip() for term in search_terms if term.strip().isdigit()]
            if case_numbers:
                missing_cases = self.update_missing_cases(case_numbers)
                self.display_missing_cases(missing_cases)
        else:
            self.results_display.setText("No folders found based on your search criteria.")

    def setup_case_checker_ui(self):
        # Case checker section
        case_checker_group = QGroupBox("Case Checker")
        case_checker_layout = QVBoxLayout()

        # Case numbers input
        case_input_layout = QHBoxLayout()
        self.case_numbers_input = QLineEdit()
        self.case_numbers_input.setPlaceholderText("Enter case numbers (comma-separated)")
        check_cases_button = QPushButton("Check Cases")
        check_cases_button.clicked.connect(self.check_missing_cases)
        case_input_layout.addWidget(self.case_numbers_input)
        case_input_layout.addWidget(check_cases_button)
        case_checker_layout.addLayout(case_input_layout)

        # Results display
        self.missing_cases_display = QTextEdit()
        self.missing_cases_display.setReadOnly(True)
        self.missing_cases_display.setMaximumHeight(100)
        case_checker_layout.addWidget(QLabel("Missing Cases:"))
        case_checker_layout.addWidget(self.missing_cases_display)

        case_checker_group.setLayout(case_checker_layout)
        self.layout.addWidget(case_checker_group)

    def check_missing_cases(self):
        if not self.source_directory:
            QMessageBox.warning(self, "Error", "Please select a source directory first.")
            return

        case_numbers = [num.strip() for num in self.case_numbers_input.text().split(',') if num.strip()]
        if not case_numbers:
            QMessageBox.warning(self, "Error", "Please enter valid case numbers.")
            return

        missing_cases, found_cases = self.case_checker.find_missing_cases(self.source_directory, case_numbers)
        
        # Update the display
        self.missing_cases_display.clear()
        if missing_cases:
            self.missing_cases_display.setTextColor(Qt.red)
            self.missing_cases_display.append("Missing case numbers:")
            for case in missing_cases:
                self.missing_cases_display.append(f"• {case}")
        else:
            self.missing_cases_display.setTextColor(Qt.green)
            self.missing_cases_display.append("No missing cases.")

        # Show summary in status bar
        total_cases = len(case_numbers)
        found_count = len(found_cases)
        missing_count = len(missing_cases)
        self.statusBar().showMessage(
            f"Total cases: {total_cases} | Found: {found_count} | Missing: {missing_count}"
        )

        # If there are missing cases, show a warning dialog
        if missing_cases:
            QMessageBox.warning(
                self,
                "Missing Cases",
                f"Found {missing_count} missing cases.\nPlease check the Missing Cases section for details."
            )


    def setup_ui(self):
        # Source directory selection
        source_layout = QHBoxLayout()
        self.source_input = QLineEdit()
        source_button = QPushButton("Select Source Directory")
        source_button.clicked.connect(self.select_source_directory)
        source_layout.addWidget(self.source_input)
        source_layout.addWidget(source_button)
        self.layout.addLayout(source_layout)

        # Search options
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.perform_search)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        self.layout.addLayout(search_layout)

        # Results display
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        self.layout.addWidget(self.results_display)

        # Action buttons
        action_layout = QHBoxLayout()
        copy_all_button = QPushButton("Copy All")
        copy_all_button.clicked.connect(lambda: self.perform_action(1))
        copy_stl_button = QPushButton("Copy STL")
        copy_stl_button.clicked.connect(lambda: self.perform_action(2))
        rename_stl_button = QPushButton("Rename STL")
        rename_stl_button.clicked.connect(lambda: self.perform_action(3))
        rename_structure_button = QPushButton("Rename Structure")
        rename_structure_button.clicked.connect(lambda: self.perform_action(4))
        action_layout.addWidget(copy_all_button)
        action_layout.addWidget(copy_stl_button)
        action_layout.addWidget(rename_stl_button)
        action_layout.addWidget(rename_structure_button)
        self.layout.addLayout(action_layout)

        # File monitoring status
        self.monitoring_status = QLabel("File monitoring: Not started")
        self.layout.addWidget(self.monitoring_status)

        # Add a Clear Missing Cases button
        clear_missing_button = QPushButton("Clear Missing Cases")
        clear_missing_button.clicked.connect(self.clear_missing_cases)
        self.layout.addWidget(clear_missing_button)

         # Add Zip Extraction button
        extract_zip_button = QPushButton("Extract ZIP")
        extract_zip_button.clicked.connect(self.extract_zip_files)
        action_layout.addWidget(extract_zip_button)

    
    def clear_missing_cases(self):
        self.missing_cases_display.clear()
        self.missing_cases_display.append("No missing cases.")

    def select_source_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        if directory:
            self.source_directory = directory
            self.source_input.setText(directory)

    def perform_search(self):
        if not self.source_directory:
            QMessageBox.warning(self, "Error", "Please select a source directory first.")
            return

        search_terms = self.search_input.text().split(',')
        found_folders = self.folder_searcher.search_by_name(self.source_directory, search_terms)

        if found_folders:
            self.results_display.clear()
            self.results_display.append("Found folders/files:")
            for name, path in found_folders.items():
                self.results_display.append(f"{name}: {path}")
        else:
            self.results_display.setText("No folders found based on your search criteria.")

    def perform_action(self, action_choice):
        if not self.source_directory:
            QMessageBox.warning(self, "Error", "Please select a source directory first.")
            return

        target_directory = QFileDialog.getExistingDirectory(self, "Select Target Directory")
        if not target_directory:
            return

        found_folders = self.get_found_folders()
        if not found_folders:
            QMessageBox.warning(self, "Error", "No folders found. Please perform a search first.")
            return

        if action_choice == 1:
            self.folder_manager.copy_contents(target_directory, found_folders)
        elif action_choice == 2:
            self.stl_handler.copy_stl_files(list(found_folders.values()), target_directory)
        elif action_choice == 3:
            self.stl_handler.copy_stl_files(list(found_folders.values()), target_directory, rename=True)
        elif action_choice == 4:
            self.stl_handler.rename_stl_files_with_structure(list(found_folders.values()), target_directory)

        QMessageBox.information(self, "Success", "Action completed successfully.")

    def get_found_folders(self):
        results = self.results_display.toPlainText().split('\n')[1:]  # Skip the "Found folders/files:" line
        found_folders = {}
        for line in results:
            if ': ' in line:
                name, path = line.split(': ', 1)
                found_folders[name] = path
        return found_folders

    def start_file_monitoring(self):
        directory_to_watch = r"\\NAKA-APP03\3Shape Dental System Orders\ManufacturingDir"
        self.file_monitor_thread = FileMonitorThread(directory_to_watch, self.log_file)
        self.file_monitor_thread.file_event.connect(self.update_monitoring_status)
        self.file_monitor_thread.start()
        self.monitoring_status.setText(f"File monitoring started: {directory_to_watch}")

    def update_monitoring_status(self, event):
        self.monitoring_status.setText(f"File event: {event}")

    

    def extract_zip_files(self):
        if not self.source_directory:
            QMessageBox.warning(self, "Error", "Please select a source directory first.")
            return

        zip_files = [f for f in os.listdir(self.source_directory) if f.endswith('.zip')]
        if not zip_files:
            QMessageBox.information(self, "No ZIP Files", "No ZIP files found in the source directory.")
            return

        target_directory = QFileDialog.getExistingDirectory(self, "Select Target Directory for Extraction")
        if not target_directory:
            return

        for zip_file in zip_files:
            zip_file_path = os.path.join(self.source_directory, zip_file)
            self.zip_extractor.extract_zip_file(zip_file_path, target_directory)

        QMessageBox.information(self, "Success", f"Extracted {len(zip_files)} ZIP file(s) to {target_directory}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())