 # Student Result Tracker using Python OOP

A terminal-based Student Result Tracker built using Python Object-Oriented Programming (OOP), JSON file handling, and exception handling.

This project simulates a real-world student management system where users can add students, assign subjects and marks, calculate results, and persist data using JSON.

## Features

- Add Student
- Remove Student
- Add Subject & Marks
- Calculate Total Marks
- Calculate Percentage
- Grade Calculation
- View Student Result
- View All Students
- Data Persistence using JSON
- Auto Reload on Restart
- Exception Handling for Invalid Inputs
- Terminal-Based Interface

## Technologies Used

- Python
- OOP (Classes & Objects)
- File Handling
- JSON
- Exception Handling

## Project Structure

```txt
student_result_tracker/
│── main.py
│── student.json
│── README.md
OOP Concepts Used
Student Class

Manages:

Student ID
Student Name
Subjects
Total Marks
Percentage
Subject Class

Manages:

Subject Name
Marks
Grade Calculation
ResultManager Class

Handles:

Student Management
File Saving/Loading
Menu System
Result Display
Learning Outcomes

Through this project, I improved my understanding of:

Python OOP Design
Class Relationships
JSON Data Persistence
Exception Handling
Real-World Project Structure
Data Serialization using to_dict()
Sample JSON Data
[
    {
        "id": 100,
        "name": "Bharat",
        "subjects": [
            {
                "subject_name": "Math",
                "marks": 90
            }
        ]
    }
]
