# Task Management REST API

This is a simple REST API built with Python, Flask, and Flask-RESTful for managing tasks. The API allows you to create, read, update, and delete tasks.

## Prerequisites

- Python 3.11 or later
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/H3nryK/task-management-api.git
2. Navigate to the project directory:
    ```bash
    cd task-management-api
3. Install the required dependencies:
    ```bash
    pip install flask flask-restful flask-sqlalchemy
4. Initialize the database:
    ```bash
    py initialize_db.py

## Usage

1. Start the Flask development server:
    ```bash
    py api.py
    ```
    The API will be accessible at `http://localhost:5000/`.

2. Use a tool like Postman, cURL, or a web browser to interact with the API endpoints:

    - `GET /tasks`: Get a list of all tasks
    - `POST /tasks`: Create a new task (send JSON data in the request body)
    - `GET /tasks/<task_id>`: Get a specific task by ID
    - `PUT /tasks/<task_id>`: Update an existing task (send JSON data in the request body)
    - `DELETE /tasks/<task_id>`: Delete a task by ID

## API Documentation

For detailed API documentation, including request/response formats and examples, please refer to the [API Documentation](https://your-api-docs-url.com).

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).