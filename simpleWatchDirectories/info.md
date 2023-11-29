# Important notes
- Ensure appropriate permissions for the script to access monitored directories.
- Adjust the monitored directories as per your requirements.

# Watchdog File System Monitoring Script

## Purpose
This Python script utilizes the Watchdog library to monitor specified directories for file system changes and logs relevant actions (file creation, modification, deletion, and movement) along with timestamps and user information.

### Libraries Used
- `os`: For operating system-related functionalities.
- `time`: To handle time-related operations.
- `getpass`: To retrieve the current user's information.
- `json`: For JSON manipulation.
- `watchdog`: Library for monitoring file system events.
  - `Observer`: Monitors file system events.
  - `FileSystemEventHandler`: Defines handlers for file system events.

### Functions and Classes
- `is_actual_modification(event)`: Checks if a file has been actually modified by comparing its modification time and size.
- `MyHandler`: Subclass of `FileSystemEventHandler` that defines event handlers and log generation.

### Event Handling
- `on_any_event(event)`: Handles various file system events (creation, modification, deletion, movement).
  - Checks for valid actions and generates log entries in JSON format containing timestamp, action, file name, and user information.
  - Logs are stored in separate files per directory monitored.

### Main Execution
- Monitors specified directories for file system events.
- Starts an observer to track changes.
- Exception handling for interrupting the monitoring process.

## Usage Instructions
1. Replace the `directories_to_watch` list with the directories you want to monitor.
2. Execute the script.

### Usage Example
```python
if __name__ == "__main__":
    directories_to_watch = ['C:\\Users\\user75\\Documents', 'C:\\Users\\user75\\Downloads']
    # ... (rest of the script)
