import socket

def create_client_connection(server, port):
    """
    Creates a client socket and connects to the specified server and port.

    Args:
    - server (str): The IP address or hostname of the server to connect to.
    - port (int): The port number to connect to.

    Returns:
    - s (socket): The created socket object.
    """
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connection to hostname on the port.
    s.connect((server, port))
    print('Server: ', server)

    return s

    
def send_message_to_server(socket_, message):
    """
    Sends a message to the server using the specified socket and receives a response.

    Args:
    - socket_ (socket): The socket object to use for communication.
    - message (str): The message to send to the server.

    Returns:
    - None
    """
    # send message to server
    socket_.send(message.encode())
    print('Sent message:', message.encode())
    socket_.close()
    