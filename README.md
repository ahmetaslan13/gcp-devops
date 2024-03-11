# Simple Flask Application

This is a simple Flask application that greets visitors with a "Hello, Simple Flask application" message when accessed.

## Installation

To run this application locally, ensure you have Python and pip installed. Then, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.

### Building and Running with Docker

To build and run the application using Docker, make sure you have Docker installed on your system. Then, follow these steps:

1. Build the Docker image by running the following command in the project directory:
    ```
    docker build -t simple-flask-app .
    ```

2. Once the build process is complete, you can run the Docker container using the following command:
    ```
    docker run -p 5001:5000 simple-flask-app
    ```

3. Access the application by opening a web browser and navigating to [http://localhost:5001/](http://localhost:5001/). You should see a "Hello, Simple Flask application" message displayed on the page.

## Usage

Once the application is running, you can access it by opening a web browser and navigating to [http://localhost:5001/](http://localhost:5001/). You should see a "Hello, Simple Flask application" message displayed on the page.

## Additional Notes

- By default, the application runs on `localhost` port `5001`, mapped to the container's port `5000`.
- This is a basic example to demonstrate the setup of a Flask application using Docker. Feel free to modify and expand it according to your needs.

