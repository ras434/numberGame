#!/usr/bin/env python




from core import gfx

import sys
import traceback


# A Game represents a single instance of a game, including its maps,
# data, and everything else.
class Game(object):
    def __init__(self):
        self.x,self.y = 0,0

    # Test method
    def handle(self, c):
        if    c == "up":        self.y -= 1
        elif  c == "down":      self.y += 1
        elif  c == "left":      self.x -= 1
        elif  c == "right":     self.x += 1

        if c:
            gfx.clear()
            gfx.draw(self.x,self.y,'@')

    # Runs an interactive session of our game with the player until either
    # the player stops playing or an error occurs.  Here, we pass input to the
    # world until we are told we don't need to anymore.  If an error occurs, we
    # turn off graphics, print the traceback, and kill the program.
    def play(self):
        gfx.start()

        try:
            running = True
            while running:
                c = gfx.get_input()
                self.handle(c)
                if c == "q": running = False
        except:
            gfx.stop()
            print(traceback.format_exc())
            exit(-1)

        gfx.stop()
