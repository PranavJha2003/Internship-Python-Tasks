# Python API Client and Data Parser

## Overview
This project retrieves user information from a public REST API,
parses the JSON response, processes the data using Pandas,
and exports the results to a CSV file.

## Technologies Used
- Python
- Requests
- REST API
- JSON
- Pandas
- Unittest

## Project Features
- Fetches user data using HTTP GET requests.
- Handles unsuccessful HTTP responses.
- Validates API response structure.
- Extracts user details from nested JSON.
- Converts data into a Pandas DataFrame.
- Exports processed data into CSV format.
- Includes automated unit tests.

## Installation

Install dependencies:

python -m pip install -r requirements.txt

## Run Application

python main.py

## Run Unit Tests

python -m unittest discover -s tests -v

## API Used

https://jsonplaceholder.typicode.com/users

## Test Results

All 7 unit tests passed successfully.