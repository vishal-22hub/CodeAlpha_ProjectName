This repository serves as a centralized collection of the software projects I developed during my internship. These applications focus on Python fundamentals, automation, and logical problem-solving, ranging from interactive games to utility tools for file management and financial tracking.

📂 Projects Overview
1. Simple Rule-Based Chatbot (CHATBOT.PY)
A conversational script that utilizes conditional logic to interact with users.

Core Logic: Implements an infinite while loop with if-elif-else structures to process natural language input.

Key Features:

Input normalization (lowercase conversion) for consistent matching.

Predefined responses for greetings and status inquiries.

Clean exit command to terminate the session.

2. Stock Portfolio Tracker (stockportfolio.py)
A financial management tool that allows users to calculate the total value of their stock holdings based on real-time-simulated pricing.

Core Logic: Uses a dictionary-based data structure to map stock symbols to prices and manages user-specific quantities.

Key Features:

Interactive CLI to add stocks and specify quantities.

Automatic calculation of individual asset totals and a grand portfolio total.

Data Persistence: Includes an option to export the final summary into a .txt report.

3. Hangman Game (HangmanGame.py)
A classic word-guessing game designed to demonstrate state management and string manipulation.

Core Logic: Utilizes the random module for word selection and tracks user progress through list comparisons.

Key Features:

Dynamic display of the word state (e.g., p _ t h _ n).

Attempt tracking with a countdown system (6 lives).

Input validation to prevent duplicate guesses or invalid characters.

4. Photo Organizer Utility (PHOTOMANAGER.PY)
An automation script designed to streamline file management by sorting specific media types.

Core Logic: Leverages the os and shutil libraries to interact with the local file system.

Key Features:

Automated directory creation for destination folders.

Batch processing: Identifies all .jpg files in a source directory.

Safe file relocation using move operations and real-time logging of moved items.

🛠 Tech Stack & Skills
Language: Python 3.x

Libraries: os, shutil, random

Concepts Demonstrated:

File I/O and File System Manipulation

Data Structures (Dictionaries, Lists, Tuples)

Error Handling (try-except blocks)

Looping & Conditional Flow Control
