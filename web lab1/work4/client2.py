import socket
import threading


def receive_messages(client_socket):
    """
    Получает сообщения от сервера и выводит их на экран.
    """
    while True:
        try:
            message = client_socket.recv(4096).decode()
            if not message:
                break
            print(message)
        except:
            print("Соединение с сервером разорвано.")
            break


def start_client():
    """
    Запускает клиентское приложение.
    """
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Адрес и порт сервера
    server_address = ('localhost', 12347)

    try:
        # Подключаемся к серверу
        client_socket.connect(server_address)
        print("Подключение к серверу установлено.")

        # Запускаем поток для получения сообщений
        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,)
        )
        receive_thread.start()

        # Отправляем сообщения на сервер
        while True:
            message = input()
            client_socket.send(message.encode())
    except:
        print("Ошибка подключения к серверу.")
    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()