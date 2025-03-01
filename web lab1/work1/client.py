import socket


def start_client():
    # Создаем UDP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Адрес и порт сервера
    server_address = ('localhost', 123)

    # Сообщение для отправки
    message = "Hello, server"

    try:
        # Отправляем сообщение серверу
        print(f"Отправка сообщения серверу: {message}")
        client_socket.sendto(message.encode(), server_address)

        # Получаем ответ от сервера
        data, server = client_socket.recvfrom(4096)
        print(f"Получен ответ от сервера: {data.decode()}")

    finally:
        # Закрываем сокет
        client_socket.close()


if __name__ == "__main__":
    start_client()