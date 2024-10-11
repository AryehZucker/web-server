# Simple HTTP Server in Python

This project implements a simple HTTP server in Python that allows users to host a website from their local machine. By running the server, others on the same network can access the hosted site.

## How It Works

The server operates as follows:

1. **Setup**: The user sets the working directory to the one containing the website files.
2. **Running the Server**: To start the server, simply run the Python script. The server listens for incoming connections on port 80, the standard port for HTTP.
3. **Handling Requests**: The server is designed to handle only HTTP GET requests. When a request is received, it checks the requested path for security risks related to directory traversal, ensuring that only valid files are accessible. If a directory is requested, it automatically serves `index.html`.
4. **Output**: For each connection, the server logs:
    - The IP address of the connecting computer.
    - The port the connection was accepted on.
    - The received HTTP request.
    - The HTTP response: `200 OK` for a valid request, `404 Not Found` for missing files, or `400 Bad Request` for invalid requests.

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

    Since port 80 is a privelaged port, administrator privelages may be required (e.g. `sudo` for Linux)

3. The server will display the local machine’s IP address, which other users on the network can use to access the hosted website via a browser.

## Security

The server includes checks for directory traversal attacks, ensuring that connecting hosts cannot access files outside of the designated directory.
