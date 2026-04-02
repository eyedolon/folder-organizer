# Folder Organizer CLI Tool

A simple Python script to organize files and folders into categorized directories.

## Features

* Sorts files into folders based on type (PDFs, images, documents, archives, etc.)
* Allows specifying a custom path via command line argument (`--path`)
* Optional verbose mode for detailed output (`--verbose`)
* Minimal progress indication in non-verbose mode

## Limitations

* No protection against overwriting files. If a file with the same name exists in the destination folder, it may be overwritten or cause an error depending on the system.
* File extension checks are case-sensitive (e.g., `.PDF` may not be recognized as `.pdf`)
* No undo functionality

## Usage

Run the script from the command line:

```bash
python organizer.py
```

Optional arguments:

```bash
python organizer.py --path /your/folder
python organizer.py --verbose
```

## Arguments

* `--path`
  Path to the folder to organize (default: `~/Downloads`)

* `--verbose`
  Prints detailed information about each processed file

## How it works

The script scans the selected directory, creates predefined folders if necessary, and moves files into those folders based on their file type.

## Future improvements

* Add overwrite protection (e.g., renaming or skipping duplicates)
* Case-insensitive file handling
* Dry-run mode
* Improved progress indication
* Logging instead of print statements

## Requirements

* Python 3
* No external dependencies (standard library only)
