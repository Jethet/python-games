# import Tkinter module as tk
import tkinter as tk
from turtle import window_height

# create an instance of the tk.Tk class => this creates the application window
root = tk.Tk()
root.title("First tutorial with Tkinter")
# root.geometry("600x400-30+150")

# TO CENTER THE WINDOW ON A SCREEN:
window_width = 300
window_height = 200
# get dimensions of the screen with the winfo_ method:
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point:
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set position of window to the center of screen with geometry():
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.attributes("-alpha", 0.5)
# add a component = widget
message = tk.Label(root, text = "Hello World!\nThis is just testing out")
message.pack()
# this works the same as the following:
# tk.Label(root, text = "Hello World!\nThis is just testing out").pack()
# button = tk.Button(_Color="black")


# call the mainloop() method of the main window object => this keeps the window
# visible on the screen and keeps it running until you close it (use it as last
# statement in the programme)
root.mainloop()