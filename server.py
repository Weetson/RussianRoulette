import socket

class Server():

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.players = []

    def host(self, host, port):
        self.server.bind((host, port))
        self.server.setblocking(0)
        self.server.listen(1)

        # Accepting player's connections
        self._host_get_client()
        
        # Getting data sent from players
        self._host_get_data()
        
        # Sending data to players
        self._host_send_data("fuck u")
            
    def connect(self, host, port):
        self.server.connect((host, port))
        
        

    def _host_get_client(self):
        try:
            client, addr = self.server.accept()
            print(f'Connected {addr}')
            client.setblocking(0)
            self.players.append(client)
        except Exception:
            print("Nobody")

    def _host_get_data(self):
        try:
            for sock in self.players:
                data = sock.recv(1024).decode()
                print(f'Got {data}')
        except Exception:
            pass
    
    def _host_send_data(self, data):
        try:
            for sock in self.players:
                sock.send('Data'.encode())
                print(f'Sent data')
        except Exception:
            self.players.remove(sock)
            sock.close()

    