import socket
from urllib.parse import parse_qs

# Used to store subject information and their grades
subjects = {}

def handle_request(request):
    """
    Handles the HTTP request and returns the corresponding HTTP response.
    """
    headers = request.split('\n')
    method = headers[0].split()[0]
    path = headers[0].split()[1]

    print(f"Method: {method}, Path: {path}")

    if method == 'GET' and path == '/':
        # Return an HTML page with the grading form
        response_body = """
        <html>
            <body>
                <h1>Subject Grades</h1>
                <form method="post" action="/">
                    <label for="subject">Subject:</label>
                    <input type="text" id="subject" name="subject" required><br>
                    <label for="grade">Grade:</label>
                    <input type="number" id="grade" name="grade" min="1" max="10" required><br>
                    <button type="submit">Add Grade</button>
                </form>
                <h2>Grades List:</h2>
                <ul>
        """
        for subject, grades in subjects.items():
            response_body += f"<li><strong>{subject}:</strong> {', '.join(map(str, grades))}</li>"
        response_body += """
                </ul>
            </body>
        </html>
        """
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{response_body}"

    elif method == 'POST' and path == '/':
        # Process the POST request and add the grade
        content_length = None
        for header in headers:
            if 'Content-Length:' in header:
                content_length = int(header.split(':')[1].strip())
                break
        body = request.split('\r\n\r\n')[1]  # 获取请求体
        data = parse_qs(body)

        print(f"Received data: {data}")

        subject = data.get('subject', [''])[0]
        grade = data.get('grade', [''])[0]

        if subject and grade:
            if subject not in subjects:
                subjects[subject] = []
            subjects[subject].append(int(grade))

        # Redirect back to the main page
        response = "HTTP/1.1 303 See Other\r\nLocation: /\r\n\r\n"

    else:
        # Return 404 Not Found
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>"

    print(f"Response: {response}")
    return response

def start_server():
    """
    Starts the server and waits for client connections.
    """
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the address and port
    server_address = ('localhost', 8080)
    server_socket.bind(server_address)

    # Listen for client connections
    server_socket.listen(5)
    print(f"Server started on {server_address}. Waiting for connections...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address}")

        try:
            # Receive the HTTP request
            request = client_socket.recv(4096).decode()
            print(f"Request received:\n{request}")

            # Handle the request and get the response
            response = handle_request(request)

            # Send the HTTP response
            client_socket.send(response.encode())
            print("HTTP response sent to the client.")

        except Exception as e:
            print(f"Error while handling the request: {e}")

        finally:
            # Close the connection to the client
            client_socket.close()
            print(f"Connection with client {client_address} closed.")

if __name__ == "__main__":
    start_server()