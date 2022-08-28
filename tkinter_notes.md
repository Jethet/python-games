## Tkinter

Tkinter is the built-in Python module that is used to create GUI (graphical user interface) applications. It is one of the most commonly used modules for creating GUI applications in Python as it is simple and easy to work with. The Tkinter module comes with Python. It gives an object-oriented interface to the Tk GUI toolkit.

**Basics**  
* import the Tkinter module: `import tkinter as tk`
* import the themed widgets from the Tkinter module: `from tkinter import ttk`
* create an instance of the tk.Tk class => this creates the application window: `root = tk.Tk()`
* add a component (= widget) as follows: widget = WidgetName(container, **options):
    * `container` is parent window/frame to place the widget
    * `options` is keyword/s argument/s that specify configuration of the widget
    * example: `message = tk.Label(root, text = "Hello World!")` => this creates a `label` widget that is placed on the `root` window
* to make the label visible, use the `pack()` method: `message.pack()`

Widgets | Description
------- | -----------
Button | Used to add buttons to your application (ttk widget)
Canvas | Used to draw pictures and others layouts like texts, graphics etc.
Checkbutton | Displays a number of options to the user as toggle buttons from which user can select any number of options (ttk widget)
ComboBox | Contains a down arrow to select from list of available options (ttk widget)
Entry | Used to input single line text entry from user (ttk widget)
Frame | Used as container to hold and organize the widgets (ttk widget)
Label | Used to display text or image on the screen (ttk widget)
LabelFrame | Used as a container that contains other related widgets (ttk widget)
Menu | Used to create all kinds of menu used by an application
Menubutton | A combination of a button and a menu widget; when clicked it shows a menu with choices
Message | Works like label and refers to multi-line and non-editable text
Notebook | Used to select pages of contents by clicking on tabs (ttk widget)
Progressbar | Used to give feedback to the user about the progress of a long-running task (ttk widget)
Radiobutton | Used to implement one-of-many selection as it allows only one option to be selected (ttk widget)
Scale | Used to provide a graphical slider which allows to select any value from that scale (ttk widget)
Scrollbar | Used to scroll down the contents; it provides a slide controller (ttk widget)
Separator | Places a thin horizontal or vertical rule between groups of widgets (ttk widget)
Sizegrip | Used to resize the entire application window (ttk widget)
Treeview | Used to display data in both tabular and hierarchical structures (ttk widget)
SpinBox | Allows user to select from given set of values (ttk widget)
Text | Allows user to edit multiline text and format the way it has to be displayed

---

**Tkinter window**  
* the root window is created with `root = tk.Tk()`. It has three system buttons: *Minimize*, *Maximize*, and *Close*
* change the window title with the `window.title(new_title)` method: `root.title("Window Demo example")`
* to get the current title of the window, use `title = window.title()` with no argument
* for **size of the window** use the `window.geometry(new_geometry)` method:
    * the geometry specification is width x height +-x +- y: width and height are in pixels, the x is the *horizontal* position and y is *vertical position* of the window
    * example: +50 as x means the left edge of the window is 50 pixels from the left edge of the screen; -50 means the right edge is 50 pixels from the right edge of the screen
* prevent the window from resizing with the `window.resizable(width, height)` method: `root.resizable(false, false)`
* if window is resizable, specify minimum and maximum sizes with `window.minsize(min_width, min_height)` and `window.maxsize(max_width, max_height)` methods
* for *background color*, use `root.configure(background="yellow)`
* for *transparency*, use `("-alpha)"`: from 0.0 (fully transparent) to 1.0 (fully opaque). Example: `root.attributes("-alpha", 0.5)`
* *window stacking order:* the order of windows placed on the screen, from bottom to top. The closer window is on the top of the stack and overlaps the one lower.
    * to place a window always at the top, use `window.attributes("-topmost", 1)`
    * to move a window up or down the stack, use `window.lift()` and `window.lower()` methods
* *change window icon:*
    1. prepare an image in the .ico format (a png or jpg can be converted with an online tool)
    2. place the icon in the folder that is accessible from the programme
    3. call the `iconbitmap()` method of the window object: `window.iconbitmap("./images/my_icon.ico")`
---

### Tkinter.ttk module
Tkinter has two generations of widgets:
* classic `tk` widgets, introduced in 1991
* new themed `ttk` widgets, added in 2007 => replace many (not all) classic widgets
The `tkinter.ttk` module containes all `ttk` widgets and should always be used.

To import widgets, use both:
```py
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text="Classic Label").pack()
ttk.Label(root, text="Themed Label").pack()

root.mainloop()
```

**Why use ttk widgets**  
* ttk widgets separate the code that implements the widget's behaviour from the appearance through the *styling system* (see below)
* ttk widgets have the native look and feel of the platform on which the programme runs
* ttk widgets simplify and generalise the state-specific widget behaviour (e.g. change appearance of a widget depending on its state)

The following ttk widgets *replace* the Tkinkter widgets with the same names:

    Button
    Checkbutton
    Entry
    Frame
    Label
    LabelFrame
    Menubutton
    PanedWindow
    Radiobutton
    Scale
    Scrollbar
    Spinbox

And the following widgets are *new and specific to ttk*:

    Combobox
    Notebook
    Progressbar
    Separator
    Sizegrip
    Treeview

Ttk widgets provide you with three ways to set options:
1. Use keyword arguments at widget creation: `ttk.Label(root, text='Hi, there').pack()`
2. Use a dictionary index after widget creation:
```py
label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()
```
3. Use the config() method with keyword attributes:
```py
label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()
```


**Button**  
Button widgets represent a clickable item in the applications. Typically, you use a text or an image to display the action that will be performed when clicked.

Buttons can display text in a single font. However, the text can span multiple lines. On top of that, you can make one of the characters underline to mark a keyboard shortcut.

To invoke a function or a method of a class automatically when the button is clicked, you assign its command option to the function or method. This is called the command binding in Tkinter. For example:  
```py
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
        )
```

To create a button, you use the ttk.Button constructor as follows:  
`button = ttk.Button(container, **option)` The most used code is: `button = ttk.Button(container, text, command)`  

**Messagebox**  
The messagebox module makes it possible to show window alerts. There are various functions in the tkinter.messagebox module: 
* `showinfo()` – notify that an operation completed successfully
* `showerror()` – notify that an operation was not completed due to an error
* `showwarning()` - notify that an operation was completed but something didn’t behave as expected.
Example:  `showinfo(title='Information', message='Download button clicked!')`

