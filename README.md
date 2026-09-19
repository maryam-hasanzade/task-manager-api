# Task Manager API

A simple REST API for managing tasks, built with FastAPI, SQLAlchemy, and SQLite.

## Features

- Create a new task
- Get all tasks
- Get a task by ID
- Update a task
- Delete a task
- Return a 404 error when a task is not found

## Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Project Structure

```text
task-manager-api/
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
python -m uvicorn main:app --reload --port 8001
```

5. Open the API documentation in your browser:

```text
http://127.0.0.1:8001/docs
```

## API Endpoints

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| POST   | `/task`            | Create a new task |
| GET    | `/tasks`           | Get all tasks     |
| GET    | `/tasks/{task_id}` | Get a task by ID  |
| PUT    | `/tasks/{task_id}` | Update a task     |
| DELETE | `/tasks/{task_id}` | Delete a task     |
