# University Management System

This is a web-based **University Management System** built using Django. It was developed as part of a web development course at my university. The project allows users (students and teachers) to manage courses, enrollments, and other academic-related tasks.

## Features

- **Courses**: Manage available courses for students to enroll in.
- **Teachers**: Assign teachers to courses and manage teacher information.
- **Choose/Enroll in Units**: Students can select units (courses) for each semester.
- **Drop Units**: Students can drop enrolled courses if necessary.
- **Authentication**: User registration and login system with different roles (student, teacher, admin).
- **Admin Panel**: Manage all users, courses, and enrollments via the Django admin interface.

## Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL (can be switched to SQLite)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap, Material Design (Django templates)
- **Authentication**: Django's built-in authentication system

## Setup Instructions

To run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/university-system.git
    cd university-system
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python3 manage.py migrate
    ```

5. **Create a superuser for the admin panel**:
    ```bash
    python3 manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python3 manage.py runserver
    ```

7. **Access the application**:
    - Open a browser and go to `http://127.0.0.1:8000/` to access the app.
    - To access the admin panel, go to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.



8. **Developers**: 
	- Masoud Mokhtari & Ali Rahimi