import os
from watchdog.events import FileSystemEventHandler
import time
import logging

class FileHandler(FileSystemEventHandler):
    def __init__(self, log_file):
        self.log_file = log_file

    def log_event(self, event_type, file_path):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {event_type}: {file_path}\n"
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def on_created(self, event):
        if not event.is_directory:
            self.log_event("File created", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.log_event("File modified", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.log_event("File deleted", event.src_path)