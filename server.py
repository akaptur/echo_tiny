import socket
import select

def make_listen_socket():
    HOST = "127.0.0.1"
    PORT = 1060
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    return s


if __name__ == '__main__':
    listen_sock = make_listen_socket()
    socket_list = [listen_sock]
    message = ''

    while True:
        read, write, _ = select.select(socket_list, socket_list, '')
        print "read", [s.fileno() for s in read]
        print "write", [s.fileno() for s in write]

        for sock in read:
            if sock is listen_sock:
                client, sock_no = listen_sock.accept()
                socket_list.append(client)
            else:
                message = sock.recv(128)
        
        for sock in write:
            if message:
                sock.send(message)
                message = ''

