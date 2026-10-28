
# Drone Observation CSV-to-JSON Cleaner

## Overview
A Python program that reads drone observation data from a CSV file,
cleans whitespace and missing values, and exports the cleaned records
to a formatted JSON file.

## Features
- Reads CSV data using Python's csv module.
- Removes unnecessary whitespace.
- Converts empty values to None.
- Exports cleaned records to JSON.
- Handles missing files and invalid CSV data.
- Includes automated unit tests using unittest.

## Project Structure
- main.py: Main CSV cleaning and JSON conversion logic.
- observations.csv: Sample input data.
- output/observations.json: Generated JSON output.
- tests/test_cleaner.py: Unit tests.

## Requirements
- Python 3.10 or newer
- No external packages required.

## How to Run

Activate the virtual environment on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Run the converter:

    python main.py

## Run Tests

    python -m unittest discover -s tests -v

## Output
The cleaned records are saved to
output/observations.json.
