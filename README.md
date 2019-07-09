# numberGame
&emsp;
*v1.1 - RAS434, 2019Jul09; https://github.com/ras434/numberGame*
  -- Refactored for PEP8
  -- Fixed many typos
  -- Removed unused variables  
*v1.0 - RAS434, 2016Nov30; https://github.com/ras434/numberGame*

&emsp;Number guessing game.

&emsp;Guess a number between 1 and 100.  

### FEATURES:
  * Keep track of guesses
  * Display last guess as well as all previous guesses
  * Displays the current number range (low side and high side of what has already been guessed)
  * Provides a hint to guess higher or lower along with a suggestion (half way between current high and low range)
  * Prompts you if you:
    * Guess too high or low
    * Guess out of range (1 to 100)

*Game Example*
<blockquote>
  <p>Tries: [1]</br>
  Guess a number between 50 and 100</br>
  Last guess: 50, Guess higher! Try 75.</br>
  All guesses: [50]</br>
  Your guess: </p>
</blockquote>

##### To clone with GIT:

&emsp;&emsp;
`
  $ git clone https://github.com/ras434/numberGame.git
`  


##### To start from;</br>
&emsp;*Terminal/BASH:*

&emsp;&emsp;
`
    $ python numberGame.py
`    
    <p>&emsp;&emsp;&emsp;&emsp;&emsp;- or - </p>
    &emsp;Set e**X**ecution attribute:</br></br>
&emsp;&emsp;
`
    $ chmod a+x numberGame.py
`    
    </br>&emsp;Now run directly:

&emsp;
`
    $ ./numberGame.py
`    

&emsp;*CMD:*

&emsp;&emsp;
`
  C:\PATH> python numberGame.py
`    

<blockquote>
Input/Options:</br>
  &emsp;[1...100]&emsp;&emsp;&emsp;&emsp;Your guess.  A number between 1 and 100.</br>
  &emsp;[888]&emsp;&emsp;&emsp;&emsp;&emsp;Restart game process by reloading 'numberGame.py'.</br>
  &emsp;[999]&emsp;&emsp;&emsp;&emsp;&emsp;Exit mid-game.  Game will exit after winning or if you guess 15 times.</br>
</blockquote>

### Credits:

  **Game** based on example from **Richard White**</br>
  &emsp;(Jan. 16, 2012; https://www.youtube.com/watch?v=pofWfJc3Zog)</br>
  **Restart features** based on example from **Petr Zemek**</br>
  &emsp;(_"Restarting a Python Script Within Itself"_ </br>  &emsp;https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/)</br>
  **colorama**</br>
  &emsp;(https://pypi.python.org/pypi/colorama)
