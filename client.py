import socket

HOST = "127.0.0.1"
PORT = 1060

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    while True:
        client.sendall(raw_input("Enter a message:"))
        message = client.recv(128)
        print message