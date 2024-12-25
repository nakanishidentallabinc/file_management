import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file created: {event.src_path}")
            # Add your custom logic here, e.g., logging, notifications, etc.

    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")
            # Add your custom logic here

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")
            # Add your custom logic here

def monitor_directory(path):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory_to_watch = r"\\NAKA-APP03\3Shape Dental System Orders\ManufacturingDir"
    monitor_directory(directory_to_watch)