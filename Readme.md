# DPLextract
DPLextract is a Python script that extracts file paths from a file and copies files with a .dpl extension to the DPLextract directory.

# Requirements
- Python 3.x
- os module
- shutil module

# Usage
- Place the files you want to extract in the input directory.
- Run the script file.py using Python 3.x.
- The script will read the file data, extract the file paths, and copy the files with a .dpl extension to the DPLextract directory.
- The copied files will be displayed in the console along with success or error messages.

# Notes
- If the input directory does not exist, it will be created automatically.
- If no files are found in the input directory, a ValueError will be raised, and the script will exit.
- If the DPLextract directory does not exist, it will be created automatically.
- If a file with the same name already exists in the DPLextract directory, it will not be overwritten.
- The script assumes that the file containing the file paths is in the input directory and is the only file with a .dpl extension.