import socket

def send_message_to_server(message):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()
    # host = '67.166.32.161'

    # reserve a port for your service.
    port = 12345

    # connection to hostname on the port.
    s.connect((host, port))

    # send message to server
    s.sendall(message.encode())

    # receive data from the server
    data = s.recv(1024)

    # close the connection
    s.close()

    # print the received data
    print('Received message!', data.decode())


send_message_to_server('Hello, world!')