# Overview
Our team created an educational game designed to teach elementary school students single digit multiplication tables. The game is a platformer where the player can walk side to side and jump through an obstacle course in a 2D landscape. NPC robots block the players way to the checkpoint at the end of the level, and the player must solve a math problem to pass them. The game starts on level 0 where the player must complete multiplication problems containing 0, and as the game progresses to other levels the number multiplied increases with the level. Player movement is handled by the physics engine which applies gravity, friction, drag, and collisions with walls, ceilings, and floors.

When the game starts the player is greeted with a title menu, then when the player clicks the mouse on the screen they are taken to a tutorial page. After clicking through the tutorial page level 0 starts. The players uses the up, down, left, and right arrow keys (or W-A-S-D) to move and jump. When they player approaches a robot, text appears on the screen prompting the user to press E to interact with the robot. When the player does press E, dialogue opens with a multiplication problem and four multiple choice answers. They player can then use their same movement keys to answer the problem. If the player answers correctly the robot disappears allowing the player to pass. If the player answers incorrectly the robot remains, and the player loses one of their three lives for the level. If the player loses three lives or falls off the screen they must restart the current level. To advance to the next level the player must reach the checkpoint at the end of each level. Each level is designed in such a way that the player must complete each robot's multiplication problem to advance to the end of the level, and each level gets progressively harder. Once the player successfully completes level nine they are presented with a victory screen, and from there may exit or click to return to the title menu.

# Development Environment
This game is 100% Python.  Python is an object-oriented language known for its readability, vast libraries, and diverse applications.  This program makes use of the arcade library, math library, PIL library, time library, and the random library.  The names of the libraries are self explanatory in what they are used for, but bring extra functionality and faster workflow.

The math library allows for better use of handling arithmetic.  This was especially important since our game uses a lot of math and physics in the background as well it being a game about with math challenges.  Time makes use of timed events and updating what is displayed based on change in time. And, random allows functions to be used, in particular, for multiple choice multiplication problems. Three options are randomized while one is correct.

We used the arcade library for the majority of our project to manage the in game sprites, play sounds, and render the window. The PIL library was used to read RGB values from a png image to easily create each map.

Our choice of development environments were Visual Studio Code and Atom.  We also use basic addon packages that make workflow easier and that make the code easier to read and navigate.

# Collaborators
* [Jesse Palmer](https://github.com/jmp1025)
* [Isaac Thomas](https://github.com/Itthomas)
* [Roberto Reynoso](https://github.com/RvRproduct)

# Useful Websites
* [Python Documentation](https://docs.python.org/3/)
* [Python Arcade Library](https://arcade.academy/)
* [Python Pillow Library](https://pillow.readthedocs.io/en/stable/)

# Future Work
* Include a point accrual system that can save and post to a scoreboard page every time the game is cleared.
* Make animation smoother and more immersive (robot animation for when the player answers correctly)
* Add in moving platforms
