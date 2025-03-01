import socket


def start_client():
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Адрес и порт сервера
    server_address = ('localhost', 8082)

    try:
        # Подключаемся к серверу
        client_socket.connect(server_address)
        print("Подключение к серверу установлено.")

        # Отправляем HTTP-запрос
        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        client_socket.send(request.encode())
        print("HTTP-запрос отправлен серверу.")

        # Получаем HTTP-ответ
        response = client_socket.recv(4096).decode()
        print(f"Получен HTTP-ответ:\n{response}")

    finally:
        # Закрываем соединение
        client_socket.close()
        print("Соединение с сервером закрыто.")


if __name__ == "__main__":
    start_client()