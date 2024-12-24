import os
from watchdog.events import FileSystemEventHandler
import time
import logging
from collections import defaultdict

class FileHandler(FileSystemEventHandler):
    def __init__(self, log_file, categorization_file):
        self.log_file = log_file
        self.categorization_file = categorization_file
        self.daily_counts = defaultdict(lambda: {'created': 0, 'modified': 0, 'deleted': 0})

    def log_event(self, event_type, file_path):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        date = time.strftime("%Y-%m-%d")
        log_entry = f"{timestamp} - {event_type}: {file_path}\n"
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
            
        self.daily_counts[date][event_type.lower()] += 1

    def categorize_file(self, file_path):
        file_name = os.path.basename(file_path)
        folder_path = os.path.dirname(file_path)
        if "_Tooth_" in file_name and file_name.endswith(".stl"):
            category = "Argenz Models"
            with open(self.categorization_file, 'a', encoding='utf-8') as f:
                f.write(f"{category}: {folder_path}\n")

        elif "_Tissue" in file_name and file_name.endswith(".stl"):
            category = "Implant Models"
            with open(self.categorization_file, 'a', encoding="utf-8") as f:
                f.write(f"{category}: {folder_path}\n")


    def on_created(self, event):
        if not event.is_directory:
            self.log_event("Created", event.src_path)
            self.categorize_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.log_event("Modified", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.log_event("Deleted", event.src_path)

    def get_daily_counts(self):
        return dict(self.daily_counts)


