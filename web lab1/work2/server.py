import socket
import math


def start_server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к локальному адресу и порту
    server_address = ('localhost', 1234)
    server_socket.bind(server_address)

    # Ожидаем подключения клиента
    server_socket.listen(1)
    print("Сервер запущен, ожидание подключения клиента...")

    while True:
        # Принимаем подключение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Подключен клиент: {client_address}")

        try:
            # Получаем данные от клиента
            data = client_socket.recv(4096).decode()
            print(f"Получены данные от клиента: {data}")

            # Обрабатываем данные (вычисляем гипотенузу по теореме Пифагора)
            try:
                a, b = map(float, data.split(','))
                result = math.sqrt(a ** 2 + b ** 2)
                response = f"Результат: {result}"
            except ValueError:
                response = "Ошибка: неверные данные"

            # Отправляем результат клиенту
            client_socket.send(response.encode())
            print(f"Отправлен результат клиенту: {response}")

        finally:
            # Закрываем соединение с клиентом
            client_socket.close()
            print(f"Соединение с клиентом {client_address} закрыто")


if __name__ == "__main__":
    start_server()