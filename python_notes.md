## Pygame

**Concepts, vocabulary etc. Pygame**  

* pygame is a library composed of various modules to access hardware:
  * `display`
  * `music`
  * `key` (respond to key input)
  * `event`
  * `image` (to load and display images or sprites)

* pygame classes:
  * `Surface`
    * a pygame object for representing images
    * defines a rectangular area to draw on
  * `display`
    * a window or full screen
    * this is created by using `.set_mode()`
    * the contents of a `Surface` is pushed to the display when `pygame.display.flip()` is called

**Most used:**  
* image module:
  * allows loading and saving of images
  * images are loaded into `Surface` objects and can be manipulated

* `Rect` class:
  * a special class for storing rectangular coordinates
  * used for managing and moving around of on-screen objects
  * used to manage collisions
---

**First steps**  
  * `import pygame` (import the pygame library)
  * `pygame.init()` (initialise pygame and all included modules, ready to work)
  * always close the game with `pygame.quit()`
  * create window: `win = pygame.display.set_mode((width, height))` => width/height values constitute a tuple, between brackets
  * with `pygame.display.set_caption("name")` add a name to the game window
  * pygames need a mainloop to run; the loop checks for events, collisions, mouse movements etc.; the simplest way is to use a while loop:
  ```py
  run = True
  while run:
    # do something
  ```
  * an event is anything that happens from the user (click, mousemove, etc.)
  * control the speed of the game with `pygame.time.delay()`
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
The framerate per second (FPS) is how many images you see per second. Most action games use 60 FPS: sixty images per second. In Pygame the FPS is defined as Clock: `pygame.time.Clock(x)` (where x is the number of FPS).

**Creating an item or character in a game**  
Attributes are:
* width
* height
* velocity
* x and y position in window

Example: draw a circle  
`pygame.draw.circle(win, color, (x, y), radius)`  

**Jumping** (see second_start.py code in this repo)  
Phases of a jump: move up, accelerate, hang still, move down, accelerate.  
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

It is possible to check if the hitbox is touched by another character, an object (like bullets), etc. by checking if this other has touched any part of the hitbox: between the coordinates plus the size of the char (width and height).

**Showing text in window**  
Variables needed with example code:
font = `pygame.font.SysFont("comicsans", 30, True, True)` (True stands for bold and italic)
text = `font.render("myText")` => this creates a surface that can be blit onto the screen (same as blitting an imange)

**Keys**  
To use key press for jumping, increasing speed, shooting bullets etc. write:  
    `keys = pygame.key.get_pressed()`
and use the key constants (K_ ...) as follows:
key name | represents
-------- | ---------- 
K_SPACE | space
K_UP | up arrow
K_DOWN | down arrow
K_RIGHT | right arrow
K_LEFT | left arrow

---


