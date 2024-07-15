Student Management System
This project is a simple Student Management System built with Flask, SQLAlchemy, and Flask-Login. The system allows users to register, log in, and manage student records.

Features
User registration and authentication
Add, update, and delete student records
View all student records
Installation
Prerequisites
Python 3.x
Flask
Flask-SQLAlchemy
Flask-Login


Steps
Clone the repository

git clone https://github.com/repository/student-management-system.git
cd student-management-system

Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies
pip install -r requirements.txt

Run the application
python3 run.py

Open your web browser and go to http://127.0.0.1:5000/

Usage
Routes
Home: /
About: /about
Students: /students
Add Student: /students/new
Update Student: /students/<id>/update
Delete Student: /students/<id>/delete
Register: /register
Login: /login
Logout: /logout


Description of Files
models/: Contains the SQLAlchemy models for the database.
base_model.py: BaseModel class for common model functionality.
user.py: User model for user authentication.
student.py: Student model for student records.
views/: Contains the view functions for different routes.
auth.py: Authentication routes (login, register, logout).
student.py: Student management routes (CRUD operations).
about.py: About page route.
templates/: HTML templates for rendering views.
static/: Static files such as CSS.
app.py: Main entry point for the application.
create_app.py: Factory function to create and configure the Flask application.
requirements.txt: List of dependencies.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request.
