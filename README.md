
# TV Show Data Analyzer

The TV Show Data Analyzer is a Python based, menu driven application that reads and processes TV show data from a CSV file. The program allows users to query, filter, sort, and analyze structured data through multiple interactive options.

This project was developed as part of CSC 110 (Survey of Computer Science) and demonstrates foundational programming, algorithmic thinking, and defensive programming practices.

---

## Overview

The application reads a data file containing TV show titles, ratings, release years, and scores. After loading the data, users interact with the dataset through a command line menu that supports multiple analysis operations.

The program continues to run until the user chooses to exit.

---

## Features

- Load and parse structured CSV data
- Filter TV shows by rating
- Identify the highest-scoring show within a specified year range
- Search for TV shows by title (case insensitive)
- Compute average scores for shows with a given rating
- Identify shows with higher scores than a specified title
- Sort TV shows by release year and export results to a new CSV file

---

## Technologies Used

- Python
- File I/O
- Lists and indexing
- Control flow and iteration
- Exception handling

---

## Program Flow

1. Prompt the user for a data file name
2. Read and parse the CSV file into structured lists
3. Display a menu of available operations
4. Execute the selected operation and display formatted results
5. Repeat until the user chooses to quit

---

## Error Handling and Validation

The program includes input validation and exception handling to ensure robust execution:

- Invalid file names prompt the user to re-enter a valid file
- User inputs are validated for correct data types and valid ranges
- Graceful handling of invalid menu selections
- Protection against runtime errors caused by malformed input

---

## Output

- Results are displayed in formatted tables for readability
- Sorted results can be written to a new CSV file for external use

---

## Key Concepts Demonstrated

- Modular program design using functions
- Algorithmic problem solving
- Data parsing and transformation
- Defensive programming and input validation
- Basic sorting algorithms

