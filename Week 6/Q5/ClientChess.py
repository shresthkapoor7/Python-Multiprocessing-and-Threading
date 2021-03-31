import socket
from chess import Game
import ServerChess as MyGlobals

def client_program():
    host = socket.gethostname()
    port = 100

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Enter your move")
    MyGlobals.g.startpos, MyGlobals.g.endpos = message.split()
    MyGlobals.g.placePieces()
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        message = input("Enter your move: ")
        MyGlobals.g.startpos, MyGlobals.g.endpos = message.split()
        MyGlobals.g.placePieces()
        print('Message from server: ' + data)
    client_socket.close()


if __name__ == '__main__':
    client_program()