import socket


def client_program():
    host = socket.gethostname()
    port = 100

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Enter massage for server:   ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Message from server: ' + data)
        message = input(" Enter massage for server:  ")

    client_socket.close()


if __name__ == '__main__':
    client_program()