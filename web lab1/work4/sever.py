import socket
import threading

# Словарь для хранения подключенных клиентов и их сокетов
clients = {}


def broadcast(message, sender_socket=None):
    """
    Отправляет сообщение всем подключенным клиентам, кроме отправителя.
    """
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except:
                # Если отправка не удалась, закрываем соединение
                client_socket.close()
                del clients[client_socket]


def handle_client(client_socket, client_address):
    """
    Обрабатывает соединение с клиентом.
    """
    print(f"Подключен новый клиент: {client_address}")

    # Запрашиваем имя пользователя
    client_socket.send("Введите ваше имя: ".encode())
    username = client_socket.recv(4096).decode().strip()
    clients[client_socket] = username

    # Уведомляем всех о новом пользователе
    broadcast(f"{username} присоединился к чату!", client_socket)

    while True:
        try:
            # Получаем сообщение от клиента
            message = client_socket.recv(4096).decode()
            if not message:
                break

            # Отправляем сообщение всем клиентам
            broadcast(f"{username}: {message}", client_socket)
        except:
            break

    # Удаляем клиента при отключении
    del clients[client_socket]
    client_socket.close()
    broadcast(f"{username} покинул чат.", client_socket)
    print(f"Клиент {client_address} отключен.")

def start_server():
    """
    Запускает сервер и ожидает подключения клиентов.
    """
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к локальному адресу и порту
    server_address = ('localhost', 12347)
    server_socket.bind(server_address)

    # Ожидаем подключения клиентов
    server_socket.listen(5)
    print(f"Сервер запущен на {server_address}. Ожидание подключений...")

    while True:
        # Принимаем подключение от клиента
        client_socket, client_address = server_socket.accept()

        # Создаем поток для обработки клиента
        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        client_thread.start()

if __name__ == "__main__":
    start_server()