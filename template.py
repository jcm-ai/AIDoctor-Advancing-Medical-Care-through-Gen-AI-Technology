import os
from pathlib import Path
import logging

# Configure logging to display information level messages with timestamps
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files to be created
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "notebook/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"
]

def create_files_and_directories(file_list):
    """
    Creates directories and files listed in file_list.
    For each file in the list, if its directory does not exist, it creates the directory.
    If the file does not exist or is empty, it creates an empty file.

    Args:
        file_list (list): List of file paths to be created.
    """
    for filepath in file_list:
        filepath = Path(filepath)
        filedir = filepath.parent

        # Create the directory if it does not exist
        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir}")

        # Create an empty file if it does not exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            filepath.touch()
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filepath} already exists")

# Run the function to create the files and directories
create_files_and_directories(list_of_files)
