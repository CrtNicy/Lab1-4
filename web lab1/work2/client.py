import socket

def start_client():
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Адрес и порт сервера
    server_address = ('localhost', 1234)

    try:
        # Подключаемся к серверу
        client_socket.connect(server_address)
        print("Подключение к серверу установлено.")

        # Вводим данные с клавиатуры
        a = float(input("Введите длину первого катета (a): "))
        b = float(input("Введите длину второго катета (b): "))
        message = f"{a},{b}"

        # Отправляем данные серверу
        client_socket.send(message.encode())
        print(f"Отправлены данные серверу: {message}")

        # Получаем результат от сервера
        data = client_socket.recv(4096).decode()
        print(f"Получен результат от сервера: {data}")

    finally:
        # Закрываем соединение
        client_socket.close()
        print("Соединение с сервером закрыто.")

if __name__ == "__main__":
    start_client()