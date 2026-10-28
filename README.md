# Internship Python Tasks

This repository contains Python assignments completed as part of the internship learning program. The assignments cover Python fundamentals, file handling, data cleaning, object-oriented programming, modular design, exception handling, and unit testing.

## Tasks

### Task 1: Python Fundamentals

**Project:** Drone Observation CSV-to-JSON Cleaner

A Python program that reads drone observation records from a CSV file, removes unnecessary whitespace, converts empty values to `None`, handles invalid input, and exports the cleaned records to JSON.

**Key concepts:**
- Python functions and collections
- CSV and JSON file handling
- Path handling using `pathlib`
- Exception handling
- Unit testing with `unittest`

**Run the project:**

```bash
cd Task1_Python_Fundamentals
python main.py
```

**Run tests:**

```bash
python -m unittest discover -s tests -v
```

### Task 2: OOP and Modular Code

**Project:** Drone Observation and Sensor Data System

A modular Python application that models drone observations and their sensor readings using object-oriented programming.

**Key concepts:**
- Classes and objects
- Inheritance and composition
- Sensor data validation
- Custom exceptions
- Modular packages and CSV processing
- Unit testing with `unittest`

**Run the project:**

```bash
cd TASK_2_OOP_Modular_Code
python main.py
```

**Run tests:**

```bash
python -m unittest discover -s tests -v
```

## Repository Structure

```text
Internship-Python-Tasks/
├── README.md
├── .gitignore
├── Task1_Python_Fundamentals/
│   ├── main.py
│   ├── observations.csv
│   ├── output/
│   ├── tests/
│   └── README.md
└── TASK_2_OOP_Modular_Code/
    ├── main.py
    ├── observations.csv
    ├── drone_project/
    ├── tests/
    └── README.md
```

## Requirements

- Python 3.10 or newer
- No third-party packages are required for the current implementations.

## Testing

Both projects include automated tests using Python's built-in `unittest` framework.

## Version Control

The repository is intended to demonstrate Git fundamentals, feature branches, commits, pull requests, code review, documentation, and issue tracking as part of the internship engineering workflow.

## Running the Tests

Run the Task 1 tests from its directory:

```powershell
cd Task1_Python_Fundamentals
python -m unittest discover -s tests -v
```

Run the Task 2 tests from its directory:

```powershell
cd ..
cd TASK_2_OOP_Modular_Code
python -m unittest discover -s tests -v
```

### Expected Results

- Task 1: 3 unit tests pass.
- Task 2: 5 unit tests pass.
- Total: 8 unit tests pass across both assignments.