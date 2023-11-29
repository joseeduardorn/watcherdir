# Important notes
- Ensure appropriate permissions for the script to access monitored directories.
- Adjust the monitored directories as per your requirements.

# Watchdog File System Monitoring Script

This Python script utilizes the Watchdog library to monitor specified directories for file system changes and logs relevant actions (file creation, modification, deletion, and movement) along with timestamps and user information.

## Code Overview
- info.md
### Libraries Used

The script utilizes several Python libraries to facilitate various functionalities:
- `os`: Handles operating system-related functionalities.
- `time`: Manages time-related operations.
- `getpass`: Retrieves the current user's information.
- `json`: Enables JSON manipulation.
- `watchdog`: Implements file system event monitoring.
  - `Observer`: Monitors file system events.
  - `FileSystemEventHandler`: Defines handlers for file system events.

### Functions and Classes

#### `is_actual_modification(event)`
Checks if a file has genuinely been modified by comparing its modification time and size.

#### `MyHandler`
Subclass of `FileSystemEventHandler` responsible for:
- Defining event handlers.
- Generating log entries containing timestamps, action types, file names, and user information.

### Event Handling

The `on_any_event(event)` function handles various file system events including:
- File creation.
- File modification.
- File deletion.
- File movement.

### Main Execution

The script:
- Monitors specified directories for file system events.
- Initiates an observer to track changes.
- Implements exception handling for interrupting the monitoring process.

The script's modular design facilitates easy customization and extension for diverse monitoring needs.

## Usage Instructions
1. Replace the `directories_to_watch` list with the directories you want to monitor.
2. Execute the script.

### Usage Example
```python
if __name__ == "__main__":
    directories_to_watch = ['C:\\Users\\user75\\Documents', 'C:\\Users\\user75\\Downloads']
    # ... (rest of the script)
