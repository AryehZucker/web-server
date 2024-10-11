# Simple HTTP Server in Python

This project implements a simple HTTP server in Python that allows users to host a website from their local machine. By running the server, others on the same network can access the hosted site.

## How It Works

The server operates as follows:

1. **Setup**: The user sets the working directory to the one containing the website files.
2. **Running the Server**: To start the server, simply run the Python script. The server listens for incoming connections on port 80, the standard port for HTTP.
3. **Handling Requests**: The server is designed to handle only HTTP GET requests. When a request is received, it checks the requested path for security risks related to directory traversal, ensuring that only valid files are accessible.
4. **Output**: While running, the server displays for each connection:
    - The IP address of the connecting computer.
    - The port the connection was accepted on.
    - The received HTTP request.
    - The HTTP response indicating whether the requested file exists or not.

## Requirements

- Python (compatible with all major operating systems: Windows, macOS, Linux).
- Only the built-in `socket` and `os` libraries are used. No additional dependencies are required.

## Usage

To run the server:

1. Change the working directory to the one containing your website files.
2. Execute the Python script:
```
python web-server.py
```

## Security

The server includes checks for directory traversal attacks, ensuring that connecting hosts cannot access files outside of the designated directory.
