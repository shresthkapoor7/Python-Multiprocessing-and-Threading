from chess import Game

import socket

g=Game()
x=0
def server_program():
    host = socket.gethostname()
    port = 100

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Client Connection from: " + str(address))
    g.startpos, g.endpos = input(' Enter Move for white: ').split()
    g.placePieces()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Message from client: " + str(data))
        g.startpos, g.endpos = input(' Enter Move for white: ').split()
        g.placePieces()

    conn.close()


if __name__ == '__main__':
    server_program()