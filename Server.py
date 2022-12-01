import socket
import time

class Server():

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.players = []

    def host(self, host, port):
        self.server.bind((host, port))
        self.server.setblocking(0)
        self.server.listen(6)
            
    def connect(self, host, port):
        self.server.connect((host, port))            

    def host_get_client(self):
        try:
            client, addr = self.server.accept()
            client.setblocking(0)
            self.players.append(client)
            return f'Connected {addr}'
        except Exception:
            return 'Nobody'

    def host_get_data(self):
        try:
            for sock in self.players:
                return sock.recv(1024).decode()
        except Exception:
            return 'Non data'
    
    def host_send_data(self, data):
        try:
            for sock in self.players:
                sock.send(data.encode())
        except Exception:
            self.players.remove(sock)
            sock.close()

    def connect_get_data(self):
        try:
            return self.server.recv(1024).decode()
        except Exception:
            return ''

    def connect_send_data(self, data):
        try:
            self.server.send(data.encode())
        except Exception:
            pass
    