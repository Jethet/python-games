**Concepts,vocabulary etc. pygame**  

* pygame is a library composed of various modules to access your hardware etc:
  * `display`
  * `music`
  * `key` (respond to key input)
  * `event`
  * `image` (to load and display images or sprites)

* first steps:
  * `import pygame` (import the pygame library)
  * `pygame.init()` (initialise pygame and all included modules, ready to work)
  * always close the game with `pygame.quit()`

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



