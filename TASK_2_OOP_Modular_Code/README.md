# Drone Observation and Sensor Data System

## Overview
A modular Python project that manages drone observations and sensor readings using object-oriented programming (OOP).

## Features
- Uses classes to represent drone observations and sensor data.
- Demonstrates inheritance and composition.
- Validates sensor readings and drone observation data.
- Uses custom exceptions for error handling.
- Loads drone observations from a CSV file.
- Includes automated unit tests using Python's unittest module.

## Project Structure
- `main.py` — Main program entry point.
- `drone_project/sensors.py` — Sensor classes and validation.
- `drone_project/observation.py` — Drone observation model.
- `drone_project/data_handler.py` — CSV loading and data processing.
- `drone_project/exceptions.py` — Custom exceptions.
- `tests/test_drone_project.py` — Unit tests.
- `observations.csv` — Sample drone observation data.

## Requirements
- Python 3.10 or later (or a compatible Python version).

## How to Run
From the project root directory, run:

```bash
python main.py
```

## How to Run Tests

```bash
python -m unittest discover -s tests -v
```

## Test Results
The project currently passes all five unit tests covering humidity validation, invalid drone IDs, CSV loading, observation composition, and temperature sensor inheritance.
