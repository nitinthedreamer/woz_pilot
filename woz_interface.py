import tkinter as tk
from client import create_client_connection, send_message_to_server


def send_text(textbox):
    """
    This function retrieves the text from the textbox and sends it to the server.
    It then clears the textbox.
    """
    text = textbox.get("1.0", "end-1c")
    socket_ = create_client_connection(server, port)
    send_message_to_server(socket_, text)
    textbox.delete("1.0", "end")
    socket_.close()
    return text

def create_textbox(root):
    """
    This function creates a textbox widget with a specified width, height and font.
    It then packs the widget and returns it.
    """
    textbox = tk.Text(root, width=80, height=15, font=("Verdana", 16))
    textbox.pack(padx=30, pady=30)
    return textbox

def create_button(root, textbox):
    """
    This function creates a button widget with a specified text, command, height, width, background color, foreground color and font.
    It then packs the widget and returns it.
    """
    button = tk.Button(root, text="Send", command=lambda: send_text(textbox), height=2, width=10, bg="blue", fg="white", font=("Verdana", 16))
    button.pack()
    return button

def create_root():
    """
    This function creates a root window with a specified title and geometry.
    It then returns the root window.
    """
    root = tk.Tk()
    root.title("Wizard")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (800 / 2))
    y = int((screen_height / 2) - (600 / 2))
    root.geometry(f"800x600+{x}+{y}")
    return root

def create_woz_interface():
    """
    This function creates a root window, a textbox widget and a button widget.
    It then runs the main loop of the root window.
    """
    root = create_root()
    textbox = create_textbox(root)
    button = create_button(root, textbox)
    root.mainloop()

server = input('Enter server IP address: ')
port = 12345

create_woz_interface()
