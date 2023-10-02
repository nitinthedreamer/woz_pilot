import socket
from participant_interface import create_participant_interface

def listen_to_client():
    """
    Listens to incoming client connections and receives data from them.
    """
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = '0.0.0.0'

    # reserve a port for your service.
    port = 12345

    # bind the socket to a public host, and a well-known port
    s.bind((host, port))

    # become a server socket
    s.listen(1)

    while True:
        # establish a connection
        print('Waiting for connection...')
        conn, addr = s.accept()
        print('Connected by', addr)
    
        # receive data from client
        data = conn.recv(1024)
        print('Received message:', data.decode())
        # close the connection
        conn.close()
        create_participant_interface(data.decode())

# Call the listen_to_client function to start listening for incoming connections
listen_to_client()
