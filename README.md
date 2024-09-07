# Python HTTP Server

This project is a basic HTTP server built using Python's `socket` library. It listens for HTTP GET requests and serves different content based on the request's path.

## Features

- **Handles GET Requests:** The server currently supports `GET` requests.
- **Serves Static HTML Files:** The root path (`/`) serves a local HTML file (`index.html`).
- **Redirects:** The `/portfolio` path redirects to a personal portfolio hosted on GitHub Pages.
- **Connection Handling:** The server listens for incoming connections and handles up to 5 queued connections.
- **Graceful Error Handling:** Requests other than `GET` are handled with a `405 Method Not Allowed` response.

## Project Structure
├── index.html # The default HTML page served at the root path 
├── server.py # Python script containing the server implementation 
└── README.md # Project documentation

## How to Run

1. Clone the repository or download the files.
2. Make sure Python 3.x is installed on your machine.
3. Open a terminal and navigate to the project directory.
4. Run the server using the following command:
   ```bash
   python server.py
5. The server will start listening on 0.0.0.0:8080. You can access it via a browser by going to http://localhost:8080. Alternativly you can access it on other local network devices by going to http://hostmachineip:8080

## Paths
- /: Serves the index.html file.
- /portfolio: Redirects to the GitHub Pages portfolio.

## Example HTTP Requests
- GET /: Returns the contents of index.html.
- GET /portfolio: Redirects the user to a specified portfolio page.
- Other Methods: Responds with a 405 Method Not Allowed.

## Future Enhancements
- Add support for POST, DELETE, and other HTTP methods.
- Implement error handling for missing files or incorrect paths.
- Improve security by handling invalid requests more gracefully.

## License
This project is licensed under the MIT License.
