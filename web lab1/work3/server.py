import socket
import os  # 新增模块


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8082)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Сервер запущен, ожидание подключения клиента...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключен клиент: {client_address}")

        try:
            request = client_socket.recv(4096).decode()
            print(f"Получен HTTP-запрос:\n{request}")

            # 使用绝对路径定位 index.html
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, 'index.html')  # 关键修改

            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html\r\n"
                    f"Content-Length: {len(content)}\r\n"
                    "\r\n"
                    f"{content}"
                )
            except FileNotFoundError:
                response = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: text/html\r\n"
                    "\r\n"
                    "<h1>404 Not Found</h1>"
                )

            client_socket.send(response.encode())
            print("HTTP-ответ отправлен клиенту.")

        finally:
            client_socket.close()
            print(f"Соединение с клиентом {client_address} закрыто.")


if __name__ == "__main__":
    start_server()