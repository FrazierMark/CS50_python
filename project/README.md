# alien_invasion

#### Video Demo: https://www.youtube.com/watch?v=Wwy4gMxENNs&feature=youtu.be

#### Description
This is an arcade game styled after old space invaders using Pygame to learn basic Object Oriented programing.

Hit the "P" button or click "Play" to begin the game.

Use the arrow keys to manuever your ship and hit the spacebar button to fire bullets.
You can choose to hold down the space bar to continually fire bullets.

The object of the game is to destory the incoming aliens before they reach the bottom of the screen.

With every fleet destroyed, the game increases in pace.

You get a total of three ships. If you lose all three ships the game is over.

The score and level information is displayed in the top right corner of the screen. The highscore is in the center.
The number of ships left is in the top left of the screen.

I'm including LOTS of comments in the code!

The MAIN program file is alien_invasion.py wherein contains various functions that detect events, update screen information, check for collisions,
update positional information, create aliens fleets, and trigger the game to start.

Our main class is AlienInvasion in which other Classes reference in order for Classes like Ship
to access all the game resources defined in AlienInvasion. Many of the other classes like Scoreboard, Alien, and GameStats do this.

To make changes to the the game like score_scale, alien or ship speed, or speedup scale simply make that changes in settings class
and they will be applied to the game. We have an initial speed setting for the ship, bullet and alien. We also have
an initial point rating point raiting for the aliens as well as the alien fleet direction.
We call increase_speed after every level which increase the speed fo the ship, bullet, and aliens and also increases
the value of the alien points.

In the Sounds class I have multiple functions. THe first function loads the background music, adjusts the volume, and then plays the music
in a loop by calling .play(-1). The bullet_sound function loads a sound that is triggered when a bullet is fired from the ship.
And the final function is the explosion sound when a bullet collides the an alien. The volume is adjusted using set_volume().

In the bullet class we create the bullet's rectangle attribute using pygame.Rect() which requires coordinates.
We set the buillet's midtop attribute to match theh ship's midtop attribute.
The update method manages the bullet's position.When bullet fired, it moves up the screen, which corresponds
to a decreasing y-coordinate value. To update the position, we subtract the amount stored in
settings.bullet_speed from self.y. We use the value of self.y to set the value of self.rect.y
(gets position of rect on every loop to later be redrawn).
To draw the bullet we call draw_bullet(). The draw.rect() functions fills the part of the screen
defined by the bullet's rect with the color stored in self.color



References from Pygame Shmup from KidsCanCode, Python Crash Course by Eric Matthes, ClearCode, Tech With Tim.

Press 'Q' to quit.
