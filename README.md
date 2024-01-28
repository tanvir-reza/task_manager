
# Django Task Manager

## Project Overview

Briefly describe Task Manager project.

## Prerequisites

- Python 
- Django 
- PostgreSQL 

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tanvir-reza/task_manager.git
   cd your-project
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables:**
   Create a `.env` file in the project root and set the following variables:

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   # Add other necessary environment variables
   ```

   Make sure to replace `your_secret_key` and `your_database_url` with your actual secret key and database URL.

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (if needed):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

   The development server will be accessible at `http://localhost:8000/`.

## Environment Variables

- `DEBUG`: Set to `True` for development, `False` for production.
- `SECRET_KEY`: Django secret key.
- `DATABASE_URL`: URL for your database (e.g., `postgres://user:password@localhost/dbname`).

## API Endpoints

### `GET /api/tasks/`

Get a list of tasks.

**Return Data:**
- `title` : Search tasks by title.
- `description` : Search tasks by description.
- `due_date` : Filter tasks by due date.
- `priority` : Filter tasks by priority.
- `completed` : Filter tasks by completion status.

**Example Usage:**
```bash
curl -X GET "http://localhost:8000/api/tasks/?title=Task&due_date=2022-01-31&priority=High&completed=False"
```

### `POST /api/tasks/`

Create a new task.

**Parameters:**
- `title`: Task title.
- `description` : Search tasks by description.
- `due_date`: Due date for the task.
- `priority`: Priority of the task.
- `completed`: Completion status of the task.

### `GET /api/tasks/<id>/`

Get a single task Details.
Update a single .
Delete a single .

**Parameters:**
- `id`: ID of the task.

