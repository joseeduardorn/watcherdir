import os
import time
import getpass
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def is_actual_modification(event):
    if event.event_type == 'modified':
        file_path = event.src_path
        old_modified_time = os.path.getmtime(file_path)
        old_size = os.path.getsize(file_path)
        
        # Wait for a short time (e.g., 0.1 seconds) to allow the system to update the modification time
        time.sleep(0.1)
        
        new_modified_time = os.path.getmtime(file_path)
        new_size = os.path.getsize(file_path)
        
        # Check if the modification time or file size has significantly changed
        if old_modified_time != new_modified_time or old_size != new_size:
            return True
    return False

class MyHandler(FileSystemEventHandler):
    def __init__(self, directories):
        super().__init__()
        self.directories = directories
        self.log_files = {}

    def get_log_file(self, directory):
        if directory not in self.log_files:
            log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log')
            current_date = time.strftime('%Y%m%d')
            user_name = getpass.getuser()
            log_file_name = f"{current_date}_{os.path.basename(directory)}_{user_name}.log"
            log_file = os.path.join(log_folder, log_file_name)
            self.log_files[directory] = log_file
        return self.log_files[directory]

    def on_any_event(self, event):
        if event.is_directory:
            return
        
        valid_actions = ['created', 'modified', 'deleted', 'moved']
        if event.event_type not in valid_actions:
            return
        
        action = ""
        if event.event_type == 'created':
            action = 'created'
        elif is_actual_modification(event):
            action = 'modified'
        elif event.event_type == 'deleted':
            action = 'deleted'
        elif event.event_type == 'moved':
            action = f"moved from {event.src_path} to {event.dest_path}"
        
        file_name = os.path.basename(event.src_path)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        log_data = {
            "timestamp": current_time,
            "action": action,
            "file_name": file_name,
            "user": getpass.getuser()
        }
        
        for directory in self.directories:
            try:
                if os.access(directory, os.R_OK):
                    if event.src_path.startswith(directory):
                        log_file = self.get_log_file(directory)
                        with open(log_file, 'a') as file:
                            file.write(json.dumps(log_data) + '\n')
                else:
                    print(f"Warning: No read permission for directory '{directory}'")
            except Exception as e:
                print(f"Error accessing directory '{directory}': {e}")

if __name__ == "__main__":
    # Replace these paths with the directories you want to monitor
    directories_to_watch = ['C:\\Users\\josem\\Documents', 'C:\\Users\\josem\\Downloads']

    event_handler = MyHandler(directories_to_watch)
    observer = Observer()
    for directory in directories_to_watch:
        observer.schedule(event_handler, directory, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
