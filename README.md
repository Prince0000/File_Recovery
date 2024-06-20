# Data Recovery Tool

## Overview

The Data Recovery Tool is a command-line utility designed to help recover specific file types (PDF, JPG, ZIP, PNG) from removable drives. It scans the drive for file signatures, extracts the data, and saves the recovered files to a specified location on your computer.

## Requirements

- Python 3.x
- `pyfiglet` module

## Installation

Before running the script, you need to install the `pyfiglet` module. You can install it using pip:

```bash
pip install pyfiglet
```

## Usage

To run the Data Recovery Tool, simply execute the script. The main menu will guide you through the recovery process.

```bash
python data_recovery_tool.py
```

### Main Menu

1. Start Data Recovery
2. Exit

### Data Recovery Process

1. **Select "Start Data Recovery" from the menu.**
2. **Enter the drive letter of the removable drive** you want to recover data from.
3. The tool will display a progress bar while scanning the drive.
4. The recovery process will start, running separate threads for each file type (PDF, JPG, ZIP, PNG).
5. The recovered files will be saved in a `RecoveredData` directory within the current working directory.
6. Once the recovery is complete, you can choose to start another recovery or exit the program.

## Code Structure

### `Recovery` Class

This class handles the data recovery for a specified file type. It initializes with the file type and includes the `data_recovery` method that performs the actual recovery process.

```python
class Recovery:
    def __init__(self, filetype):
        self.filetype = filetype

    def data_recovery(self, fileName, fileStart, fileEnd, fileOffSet, drive_letter, recovered_location):
        # Recovery logic
```

### `progress_bar` Function

Displays a progress bar for the scanning process.

```python
def progress_bar(total_iterations, current_iteration, bar_length, fill):
    # Progress bar logic
```

### `show_menu` Function

Displays the main menu and available drives.

```python
def show_menu(recovered_location, available_drives):
    # Menu display logic
```

### `main_menu` Function

Handles the main menu logic and user inputs.

```python
def main_menu():
    # Main menu logic
```

### `start_data_recovery` Function

Manages the data recovery process, including starting threads for each file type.

```python
def start_data_recovery(pdf, jpg, zip_recovery, png, total_iteration, recovered_location, available_drives):
    # Data recovery logic
```

## Example

1. Run the script:
    ```bash
    python data_recovery_tool.py
    ```
2. Select option `1` to start data recovery.
3. Enter the drive letter of the removable drive (e.g., `E`).
4. The tool will scan the drive and recover files, displaying progress along the way.
5. Recovered files will be saved in the `RecoveredData` directory.

## Notes

- Ensure you have the necessary permissions to read from the specified drive.
- The tool is designed for specific file types (PDF, JPG, ZIP, PNG) based on their signatures.
- The recovery process may take some time depending on the size of the drive and the number of files to recover.
