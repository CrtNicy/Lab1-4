import socket


def start_server():
    # Создаем UDP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем сокет к локальному адресу и порту
    server_address = ('localhost', 123)
    server_socket.bind(server_address)

    print("Сервер запущен, ожидание сообщений от клиента...")

    while True:
        # Получаем данные от клиента
        data, client_address = server_socket.recvfrom(4096)
        print(f"Получено сообщение от {client_address}: {data.decode()}")

        # Отправляем ответ клиенту
        response_message = "Hello, client"
        server_socket.sendto(response_message.encode(), client_address)
        print(f"Ответ отправлен клиенту {client_address}: {response_message}")


if __name__ == "__main__":
    start_server()