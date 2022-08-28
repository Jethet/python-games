# import Tkinter module as tk
import tkinter as tk
from tkinter import ttk
from turtle import color, window_height

# create an instance of the tk.Tk class => this creates the application window
root = tk.Tk()
root.config(background="yellow")
root.title("First tutorial with Tkinter")
# root.geometry("600x400-30+150")

# TO CENTER THE WINDOW ON A SCREEN:
window_width = 700
window_height = 400
# get dimensions of the screen with the winfo_ method:
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point:
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set position of window to the center of screen with geometry():
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.attributes("-alpha", 0.8)
# add a component = widget
message = tk.Label(root, text = "Hello World!\nThis is just testing out\nA button has been added but needs formatting")
message.pack()
# this works the same as the following:
# tk.Label(root, text = "Hello World!\nThis is just testing out").pack()

info_message = tk.Label(root, text = "This is something I am learning and it's been a while since I have been coding in Python ;-)")
info_message.pack()

from tkinter.messagebox import showerror, showinfo
# root window
root.title('Image Button Demo')

# download button
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
        ),
    showerror(
        title="Error message",
        message="There was an error"
    )

download_icon = tk.PhotoImage(file='./download_icon.png')
download_button = ttk.Button(
    root,
    image=download_icon,
    text="Download",
    compound=tk.LEFT,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)

root.mainloop()

# call the mainloop() method of the main window object => this keeps the window
# visible on the screen and keeps it running until you close it (use it as last
# statement in the programme)
root.mainloop()