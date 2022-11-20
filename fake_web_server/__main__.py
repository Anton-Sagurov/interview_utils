import socket
import os

HOST = ""
PORT = 80

if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)

        print("Waiting for connection...")
        while True:
            sock, addr = serv_sock.accept()

            
