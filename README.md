# Personal Task Manager

## Introduction

The Personal Task Manager is a web application built with FastAPI that allows users to manage their tasks efficiently. Users can create, update, delete, and view tasks. The application also supports user authentication and maintains a history of user actions.

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite for relational data and MongoDB for logging user actions
- **ORM**: SQLAlchemy
- **Authentication**: OAuth2 with JWT tokens
- **Password Hashing**: Passlib
- **Environment Variables**: Python-dotenv

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd personal_task_manager
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv .venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    - Create a `.env` file in the [personal_task_manager](http://_vscodecontentref_/0) directory with the following content:
        ```
        DB_CONNECTION_STRING=<your-mongodb-connection-string>
        ```

## Running the Project

1. **Run the FastAPI application**:
    ```sh
    uvicorn personal_task_manager.main:app --reload
    ```

2. **Access the application**:
    - Open your browser and navigate to `http://127.0.0.1:8000`.

3. **API Documentation**:
    - FastAPI provides interactive API documentation at `http://127.0.0.1:8000/docs` (Swagger UI) and `http://127.0.0.1:8000/redoc` (ReDoc).

## Project Structure

personal_task_manager/
├── __init__.py
├── .env
├── database.py
├── hashing.py
├── main.py
├── models.py
├── routers/
│   ├── __init__.py
│   ├── authentication.py
│   ├── tasks.py
│   └── users.py
├── schemas.py
├── services/
│   ├── __init__.py
│   ├── tasks.py
│   └── users.py
├── test.ipynb
├── test.py
└── token.py
requirements.txt
README.md


## Features

- **User Authentication**: Secure user authentication using OAuth2 and JWT tokens.
- **Task Management**: Create, update, delete, and view tasks.
- **User History**: Maintain a history of user actions using MongoDB.
- **Password Hashing**: Secure password storage using Passlib.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
