# Duplicate File Remover

This Python script scans a specified directory (and all its subdirectories) to find and delete duplicate files, keeping only one original copy of each file.

## Features

- Recursively scans the specified directory and its subdirectories.
- Detects duplicate files by comparing their MD5 hashes.
- Deletes duplicate files, retaining only one copy of each unique file.
  
## Prerequisites

- **Python 3.x** is required. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Deloyers/Delete_dublicate.git
    cd duplicate-file-remover
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

## Usage

1. Open the `duplicate_file_remover.py` script in a text editor.
2. Set the `directory_path` variable to the path of the directory you want to scan for duplicates.

    ```python
    directory_path = "/path/to/your/directory"
    ```

3. Run the script:
    ```bash
    python main.py
    ```

4. The script will print a message for each duplicate file it deletes.

### Example

If you want to run the script on a directory called `test_folder`, set:

```python
directory_path = "test_folder"
