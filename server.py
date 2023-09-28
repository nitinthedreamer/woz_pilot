import socket
from tkinter import *
from sys import exit


def popupError(s):
    popupRoot = Tk()
    popupRoot.after(20000, exit)
    popupButton = Button(popupRoot, text = s, font = ("Verdana", 12), bg = "yellow", command = exit)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()


def listen_to_client():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    # reserve a port for your service.
    port = 12345

    # bind the socket to a public host, and a well-known port
    s.bind((host, port))

    # become a server socket
    s.listen(1)

    while True:
        # establish a connection
        # print('Waiting for connection...')
        conn, addr = s.accept()
        print('Connected by', addr)
    
        # receive data from client
        data = conn.recv(1024)
        # if not data:
        #     break
        print('Received message:', data.decode())
        popupError(data.decode())

        # close the connection
        conn.close()



listen_to_client()
