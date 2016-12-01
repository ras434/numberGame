# numberGame
Number guessing game

Guess a number between 1 and 100.  

FEATURES:
  * Keep track of guesses
  * Display last guess as well as all previous guesses
  * Displays the current number range (low side and high side of what has already been guessed)
  * Provides a hint to guess higher or lower along with a suggestion (half way between current high and low range)
  * Prompts you if you:
    * Guess too high or low
    * Guess out of range (1 to 100)

==========================[ Game Action ]==============================
Tries: [1]
Guess a number between 50 and 100
Last guess: 50, Guess higher! Try 75.
All guesses: [50]
Your guess: 
========================================================================

To clone with GIT:
  $ git clone https://github.com/ras434/numberGame.git
  
To start from;
  Terminal/BASH:
    $ python numberGame.py
    
    - or -
    
    Set eXecution attribute:
    $ chmod a+x numberGame.py
    
    Now run directly:
    $ ./number
    
  CMD:
    > python numberGame.py
    
Input/Options:
  [1...100]     Your guess.  A number between 1 and 100.
  [888]         Restart game process by reloading 'numberGame.py'.
  [999]         Exit mid-game.  Game will exit after winning or if you guess 15 times.
  
Credits:
  Game based on example from Richard White 
    (Jan. 16, 2012; https://www.youtube.com/watch?v=pofWfJc3Zog)
  Restart features based on example from Petr Zemek
    ("Restarting a Python Script Within Itself"; https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/)
  colorama; https://pypi.python.org/pypi/colorama
