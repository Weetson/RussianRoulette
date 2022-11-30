import Server
import time

import pretty_errors

# Innitializing server
server = Server.Server()
server.host(host = 'localhost', port = 8080)

while True:
    # Accepting player's connections
    print(server.host_get_client())
    
    # Getting data sent from players
    data = server.host_get_data()
    
    # Sending data to players
    server.host_send_data(data)

    time.sleep(0.01)