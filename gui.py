import sys
import traceback
import os
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog, QMessageBox,QGroupBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import QtGui
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
from PyQt5.QtWidgets import QTabWidget, QSplitter, QTreeView, QFileSystemModel

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLineEdit, QTextEdit, 
                             QLabel, QFileDialog, QMessageBox, QInputDialog)

class FileMonitorThread(QThread):
    file_event = pyqtSignal(str)

    def __init__(self, directory, log_file, categorization_file):
        super().__init__()
        self.directory = directory
        self.log_file = log_file
        self.categorization_file = categorization_file

    def run(self):
        event_handler = FileHandler(self.log_file, self.categorization_file)
        observer = Observer()
        observer.schedule(event_handler, self.directory, recursive=True)
        observer.start()
        try:
            while not self.isInterruptionRequested():
                self.sleep(1)
        finally:
            observer.stop()
            observer.join()
    
    def stop(self):
        self.requestInterruption()
        self.wait()







class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nakanishi Dental Lab File Management System")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(script_dir, 'file_tracking.log')
        self.categorization_file = os.path.join(script_dir, 'categorization.txt')


        


        self.setup_ui()

        self.folder_searcher = FolderSearcher()
        self.folder_manager = FolderManager()
        self.zip_extractor = ZipExtractor()
        self.stl_handler = STLFileHandler()
        self.case_checker = CaseChecker()
        self.zip_extractor = ZipExtractor()

        self.categorization_file = os.path.join(script_dir, 'categorization.txt')
        file_handler = FileHandler(self.log_file, self.categorization_file)



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

        
    def setup_enhanced_ui(self):
        # Create a tab widget for better organization
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # File management tab
        file_management_widget = QWidget()
        file_management_layout = QVBoxLayout(file_management_widget)
        self.tab_widget.addTab(file_management_widget, "File Management")

        # Create a splitter for file browser and actions
        splitter = QSplitter(Qt.Horizontal)
        file_management_layout.addWidget(splitter)

        # Add a file system tree view
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(self.source_directory)
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setRootIndex(self.file_system_model.index(self.source_directory))
        splitter.addWidget(self.tree_view)

        # Add existing widgets to the right side of the splitter
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.addWidget(self.search_input)
        right_layout.addWidget(self.results_display)
        right_layout.addLayout(self.action_layout)
        splitter.addWidget(right_widget)

        # Case checker tab
        case_checker_widget = QWidget()
        case_checker_layout = QVBoxLayout(case_checker_widget)
        case_checker_layout.addWidget(self.case_checker_group)
        self.tab_widget.addTab(case_checker_widget, "Case Checker")

        # File monitoring tab
        monitoring_widget = QWidget()
        monitoring_layout = QVBoxLayout(monitoring_widget)
        monitoring_layout.addWidget(self.monitoring_status)
        self.tab_widget.addTab(monitoring_widget, "File Monitoring")


    # ... (other existing methods) ...

    def process_filename(self):
        filename, ok = QInputDialog.getText(self, "Enter Filename", "Enter the filename:")
        if ok and filename:
            try:
                part_name = filename.split('_')[1]
                case_number = part_name[20:23]
                result = f"pan {case_number}"
                QMessageBox.information(self, "Result", result)
            except IndexError:
                QMessageBox.warning(self, "Error", "Invalid filename format")

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

        # Add File Catcher toggle button
        self.file_catcher_button = QPushButton("Start File Catcher")
        self.file_catcher_button.setCheckable(True)
        self.file_catcher_button.clicked.connect(self.toggle_file_catcher)
        self.layout.addWidget(self.file_catcher_button)



    
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
        try:
            if not self.source_directory:
                raise ValueError("Source directory not selected")

            target_directory = QFileDialog.getExistingDirectory(self, "Select Target Directory")
            if not target_directory:
                raise ValueError("Target directory not selected")

            found_folders = self.get_found_folders()
            if not found_folders:
                raise ValueError("No folders found. Please perform a search first.")

            if action_choice == 1:
                self.folder_manager.copy_contents(target_directory, found_folders)
            elif action_choice == 2:
                self.stl_handler.copy_stl_files(list(found_folders.values()), target_directory)
            elif action_choice == 3:
                self.stl_handler.copy_stl_files(list(found_folders.values()), target_directory, rename=True)
            elif action_choice == 4:
                self.stl_handler.rename_stl_files_with_structure(list(found_folders.values()), target_directory)
            else:
                raise ValueError(f"Invalid action choice: {action_choice}")

            QMessageBox.information(self, "Success", "Action completed successfully.")
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}\n\n{traceback.format_exc()}"
            QMessageBox.critical(self, "Error", error_msg)
            logging.error(error_msg)

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
        self.file_monitor_thread = FileMonitorThread(directory_to_watch, self.log_file, self.categorization_file)
        self.file_monitor_thread.file_event.connect(self.update_monitoring_status)
        self.file_monitor_thread.start()
        self.monitoring_status.setText(f"File monitoring started: {directory_to_watch}")



    def toggle_file_catcher(self):
        if self.file_catcher_button.isChecked():
            self.start_file_monitoring()
            self.file_catcher_button.setText("Stop File Catcher")
        else:
            self.stop_file_monitoring()
            self.file_catcher_button.setText("Start File Catcher")

    
    def stop_file_monitoring(self):
        if hasattr(self, 'file_monitor_thread'):
            self.file_monitor_thread.stop()
            self.file_monitor_thread.wait()
            self.monitoring_status.setText("File monitoring stopped")




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