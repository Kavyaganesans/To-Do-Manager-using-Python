 To-Do Manager using Python

Overview

The To-Do Manager is a simple yet effective task management application built using Python. This project helps users keep track of their daily tasks, allowing them to add, update, delete, and mark tasks as completed.

Features

Add new tasks with due dates and priorities

View all pending tasks

Mark tasks as completed

Delete tasks

Save and load tasks for persistence

Technologies Used

Python

Tkinter (for GUI-based application)

SQLite (for data storage)

JSON (for lightweight data storage alternative)

Installation

Clone the repository:

git clone https://github.com/yourusername/To-Do-Manager.git
cd To-Do-Manager

Install required dependencies:

pip install -r requirements.txt

Run the application:

python main.py

Usage

Open the application.

Add new tasks with descriptions and due dates.

View pending tasks and mark them as completed when done.

Delete tasks if no longer needed.

Close the application and reopen it later to continue where you left off.

File Structure

To-Do-Manager/
│── main.py        # Entry point of the application
│── gui.py         # Handles the user interface using Tkinter
│── database.py    # Manages task storage using SQLite
│── tasks.json     # Alternative JSON storage for tasks
│── README.md      # Project documentation
│── requirements.txt # List of dependencies

Future Enhancements

Implement task categories and labels

Add notifications and reminders

Sync tasks with cloud storage

License

This project is licensed under the MIT License.

Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

 
