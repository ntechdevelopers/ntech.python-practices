# Python Practices Project

This repository contains various Python practice materials and a utility for processing CSV files in bulk, primarily for educational and data management purposes.

## Project Structure

```
.
├── practices/                # PDF exercises for Python practice (in Vietnamese)
├── src/
│   └── ShareFileCSV/
│       ├── src/
│       │   ├── TranformData.py   # Main script for splitting and organizing CSV data
│       │   ├── config.json       # Configuration for the script
│       │   └── StudentOtcs.csv  # Example input CSV (large file)
│       ├── venv/                # Python virtual environment (optional)
│       └── .idea/               # IDE configuration (ignore)
└── .git/                    # Git version control
```

## ShareFileCSV Utility

### Purpose

The `ShareFileCSV` tool is designed to split a large CSV file into multiple smaller files, each containing a specified number of rows, and organize them into separate directories. This is useful for batch processing, data import/export, or distributing data in manageable chunks.

### How It Works
- Reads configuration from `config.json`.
- Loads the input CSV file (e.g., `StudentOtcs.csv`).
- Splits the data into groups, each with a maximum number of rows as specified.
- Creates output directories for each group, following a naming pattern.
- Writes each group to a new CSV file in its respective directory.

### Configuration (`config.json`)
| Key          | Description                                 | Example                |
|--------------|---------------------------------------------|------------------------|
| inputFile    | Name of the input CSV file                  | "StudentOtcs.csv"     |
| rowPerFile   | Number of rows per output file              | 500                    |
| rootOutput   | Root directory for output                   | "D:\\Data"            |
| startNumber  | Starting number for output directory naming | 50000                  |
| patternDir   | Pattern for output directories              | "data-{0}\\Data"       |

### Usage

1. **Set up your environment:**
   - (Optional) Create and activate a Python virtual environment.
   - Ensure Python 3.x is installed.

2. **Place your input CSV file** in the `src/ShareFileCSV/src/` directory (default: `StudentOtcs.csv`).

3. **Edit `config.json`** to match your desired settings.

4. **Run the script:**
   ```bash
   cd src/ShareFileCSV/src
   python TranformData.py
   ```
   Output will be created in the specified `rootOutput` directory, organized by the pattern in `patternDir`.

### Dependencies
This script uses only Python's standard library (`csv`, `os`, `json`, `math`). No external packages are required.

## practices/
This folder contains PDF files with Python exercises, suitable for beginners and intermediate learners. The exercises are in Vietnamese and cover topics such as:
- Control structures and loops
- Arrays
- String manipulation

## Notes
- The `.idea/` and `venv/` folders are for development environment configuration and can be ignored.
- The `.git/` directory is for version control and not relevant to usage.

## License
This project is for educational purposes. Please check individual files for any specific licensing information. 