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

**Creating an item or character in a game**  
Attributes are:
* width
* height
* velocity
* x and y position in window



