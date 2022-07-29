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


