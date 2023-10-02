import tkinter as tk
from PIL import ImageTk, Image
from playsound import playsound

image_path = "woz.png"

def create_textbox(root, message):
    """
    This function creates a textbox widget with a specified width, height and font.
    It then packs the widget and returns it.
    """
    
    textbox = tk.Text(root, width=80, height=15, font=("Verdana", 16))
    textbox.pack(padx=30, pady=(150+30, 30))
    textbox.insert("end", message)
    textbox.configure(state="disabled")
    return textbox


def create_button(root):
    """
    This function creates a button widget with a specified text, command, height, width, background color, foreground color and font.
    It then packs the widget and returns it.
    """
    
    button = tk.Button(root, text="Close", height=2, width=10, bg="blue", fg="white", font=("Verdana", 16), command=root.destroy)
    button.pack()
    return button

def add_image(root):
    """
    This function adds an image to the root window.
    It takes in the root window and the path to the image file as arguments.
    """
    
    img = Image.open(image_path)
    img = img.resize((150, 150))
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.pack(side="top", pady=30)
    panel.place(relx=0.5, rely=0, anchor="n")
    root.mainloop()


def create_root():
    """
    This function creates a root window with a specified title and geometry.
    It then returns the root window.
    """
    root = tk.Tk()
    root.title("Wizard Says:")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (800 / 2))
    y = int((screen_height / 2) - (600 / 2))
    root.geometry(f"800x600+{x}+{y}")
    return root

def create_participant_interface(message):
    """
    This function creates a root window, a textbox widget and a button widget.
    It then runs the main loop of the root window.
    """
    playsound('notify_participant.wav', block=False)
    root = create_root()
    textbox = create_textbox(root, message)
    button = create_button(root)
    add_image(root)
    root.mainloop()
