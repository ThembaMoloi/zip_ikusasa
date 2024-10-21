## Overview

This feature allows users to compress a specified directory into a ZIP file. It is designed to be integrated into a web-based PDF tool to enhance file management capabilities.

## Requirements

- Python 3.x
- `zipfile` module (built-in with Python)
- `os` module (built-in with Python)

## Installation

1. Ensure Python 3.x is installed on your system.
2. No additional packages are required as the script uses built-in Python modules.

## Usage
1. Run the script using a Python interpreter.

### Command Line

To use the script from the command line:

```sh
python zip_directory.py
```

### User Input

When prompted, enter the path of the directory you wish to compress.

## Code Explanation

The script contains a function `zip_directory(directory_path, zip_path)` that:

1. Creates a ZIP file at the specified path.
2. Checks if the directory to be zipped exists.
3. Walks through the directory, adding each file to the ZIP file.
4. Handles errors and provides feedback to the user.

### Functions

- `zip_directory(directory_path, zip_path)`: Compresses the specified directory into a ZIP file.
  - `directory_path`: Path of the directory to be compressed.
  - `zip_path`: Path where the ZIP file will be created.

### Main Execution

When executed as the main module, the script:
1. Prints the current working directory.
2. Prompts the user to enter the directory path to be zipped.
3. Calls `zip_directory` to perform the compression.
4. Prints the success or failure message based on the result.

## Error Handling

The script includes basic error handling:
- Checks if the specified directory exists.
- Catches and prints unexpected errors.

## Notes
- The ZIP file will be created in the same directory as the specified directory with a `.zip` extension.

