## Pygame

**Concepts,vocabulary etc. pygame**  

* pygame is a library composed of various modules to access your hardware etc:
  * `display`
  * `music`
  * `key` (respond to key input)
  * `event`
  * `image` (to load and display images or sprites)

* pygame classes:
  * `Surface`
    * a pygame object for representing images
    * defines a rectangular area on which you can draw
  * `display`
    * a window or full screen
    * this is created by using .set_mode()
    * the contents of a `Surface` is pushed to the display when `pygame.display.flip()` is called

Most used:  
* image module:
  * allows loading and saving of images
  * images are loaded into `Surface` objects and can be manipulated

* `Rect` class:
  * a special class for storing rectangular coordinates
  * used for managing and moving around of on-screen objects
  * used to manage collisions

**First steps**  
  * `import pygame` (import the pygame library)
  * `pygame.init()` (initialise pygame and all included modules, ready to work)
  * always close the game with `pygame.quit()`
  * create window: `win = pygame.display.set_mode((width, height))` => width/height values constitute a tuple, between brackets
  * with `pygame.display.set_caption("name")` you can add a name to the game window
  * pygames need a mainloop to run; the loop checks for events, collisions, mouse movements etc.; the simplest way is to use a while loop:
  ```py
  run = True
  while run:
    # do something
  ```
  * an event is anything that happens from the user (click, mousemove, etc.)
  * with `pygame.time.delay()` you can control the speed of the game
  * the window's starting point is 0, 0: the top left corner of the window
  * when moving something in the window, the window has to be refreshed every time by filling it with the background color, for example black: `win.fill((0, 0))`
  * after each event, the window has to be updated: `pygame.display.update()`

**Using images**  
Add the image to the folder. In the code, load and save it into the img variable. Use the correct image name plus extension and add this in *string* format.

To draw an image on the screen, use `Surface.blit()` (can be screen.blit() or window.blit()).  

`pygame.display.flip()` means that Pygame is buffering everything that has been drawn, to make it visible on the screen as completely drawn frames (otherwise the user will see half completed parts of the screen during creation).

To resize an image, use `pygame.transform.scale()`:
```py
img = pygame.image.load("ball.png")
ball = pygame.transform.scale(img, (65, 65))
```

**Framerate**  
The framerate per second (FPS) is how many images you see per second.  
Most action games use 60 FPS: sixty images per second. In Pygame the FPS is defined as Clock: `pygame.time.Clock(x)` (where x is the number of FPS)

**Creating an item or character in a game**  
Attributes are:
* width
* height
* velocity
* x and y position in window

Example: draw a circle  
`pygame.draw.circle(win, color, (x, y), radius)`  

**Jumping** (see second_start.py)  
What is a jump: move up, accelerate, hang still, move down, accelerate.  
For this a quadratic function is used as follows:
```py
if jumpCount >= -10:
        neg = 1
        if jumpCount < 0:
            neg = -1
        y -= (jumpCount ** 2) * 1 * neg
        jumpCount -= 1
```
**Collision**  
A character needs to have a hitbox around it to make collision or hitting it possible. The hitbox is created with x and y coordinates where the top left of the hitbox should be, and the width and height of the box to fit around the character.  
You can check if the hitbox is touched by another character, an object (like bullets), etc. by checking if this other has touched any part of the hitbox: between the coordinates plus the size of the char (width and height).

**Showing text in window**  
Variables needed with example code:
font = `pygame.font.SysFont("comicsans", 30, True, True)` (True stands for bold and italic)
text = `font.render("myText")` => this creates a surface that can be blit onto the screen (same as blitting an imange)

**Keys**  
To use key press for jumping, increasing speed, shooting bullets etc. write:  
    `keys = pygame.key.get_pressed()`
and use the key constants (K_xxx) as follows:  
K_SPACE               space
K_UP                  up arrow
K_DOWN                down arrow
K_RIGHT               right arrow
K_LEFT                left arrow

---

### Tkinter

**Basics**  
* import the Tkinter module: `import tkinter as tk`
* create an instance of the tk.Tk class => this creates the application window: `root = tk.Tk()`
* add a component (= widget) as follows: widget = WidgetName(container, **options)
* `container` is parent window/frame to place the widget; `options` is keyword/s argument/s that specify configuration of the widget
* example: `message = tk.Label(root, text = "Hello World!")` => this creates a `label` widget that is placed on the `root` window
* to make the label visible, use the `pack()` method: `message.pack()`

Widgets | Description
------- | -----------
Label | Used to display text or image on the screen
Button | Used to add buttons to your application
Canvas | Used to draw pictures and others layouts like texts, graphics etc.
ComboBox | Contains a down arrow to select from list of available options
CheckButton | Displays a number of options to the user as toggle buttons from which user can select any number of options.
RadiButton | Used to implement one-of-many selection as it allows only one option to be selected
Entry | Used to input single line text entry from user
Frame | Used as container to hold and organize the widgets
Message | Works like label and refers to multi-line and non-editable text
Scale | Used to provide a graphical slider which allows to select any value from that scale
Scrollbar | Used to scroll down the contents. It provides a slide controller.
SpinBox | Allows user to select from given set of values
Text | Allows user to edit multiline text and format the way it has to be displayed
Menu | Used to create all kinds of menu used by an application  

---

**Tkinter window**  
* the root window is created with `root = tk.Tk()`. It has three system buttons:  
*Minimize*, *Maximize*, and *Close*
* change the window title with the `window.title(new_title)` method: `root.title("Window Demo example")
* to get the current title of the window, use `title = window.title()` with no argument
* **size of the window:** use the `window.geometry(new_geometry)` method 
* the geometry specification is width x height +-x +- y: width and height are in pixels, the x is the *horizontal* position and y is *vertical position* of the window
* example: +50 as x means the left edge of the window is 50 pixels from the left edge of the screen; -50 means the right edge is 50 pixels from the right edge of the screen
* prevent the window from resizing with the `window.resizable(width, height)` method: `root.resizable(false, false)`
* if window is resizable, specify minimum and maximum sizes with `window.minsize(min_width, min_height)` and `window.maxsize(max_width, max_height)` methods
* for *transparency*, use `"-alpha"`: from 0.0 (fully transparent) to 1.0 (fully opaque). Example: `root.attributes("-alpha", 0.5)`
* *window stacking order:* the order of windows placed on the screen, from bottom to top. The closer window is on the top of the stack and overlaps the one lower. To place a window always at the top, use `window.attributes("-topmost", 1)`.
to move a window up or down the stack, use `window.lift()` and `window.lower()` methods
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