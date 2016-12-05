#!/usr/bin/env python
import random, time, sys, platform, curses
from colorama import Fore
import os

userGuesses = []

WATCHED_FILES = [__file__]		# To add files to watch, create comma seperated list [file1, file2, file3]
WATCHED_FILES_MTIMES = [(f, os.path.getmtime(f)) for f in WATCHED_FILES]

def main():
	# Initialize the program

	# Check dependancies

		# Determine if running under Windows OS

		# Determine if colorama is available

		# Install any Windows specific requirements, if needed


	global userGuesses
	checkDependancies()
	# clearScreen()						# might not need this function due to curses features
	myscreen = curses.initscr()
	myscreen.border(0)
	myscreen.addstr(12, 25, "numberGame.py")
	myscreen.refresh()
	# myscreen.getch()
	time.sleep(1)
	curses.endwin()
	print("Guess a number between 1 and 100.")
	time.sleep(1)
	print("Type '" + Fore.YELLOW + "999" + Fore.RESET + "' to exit game.")
	time.sleep(1)
	# randomNumber = 35
	tries = 0
	randomNumber = random.randint(1,100)
	found = False		# flag variable to see if they guessed
						# it
	hint = ""
	userGuess = ""
	lastGuess = ""
	highGuess = 100
	lowGuess = 1

# Run through the guessing process
	while not found:
		clearScreen()
		checkFiles()
		print("Tries: [" + str(tries) + "]\nGuess a number between " + str(lowGuess) + " and " + str(highGuess))
		if len(userGuesses)>0:
			print("Last guess: " + str(userGuess) + ", " + hint)
			hint = ""
			allGuesses()	# Display all Guesses
		else:
			print("\n")
		if len(userGuesses) > 15:
			import subprocess as sp
			tmp = sp.call('say you should probably try something easier',shell=True)
			print("You should probably try something easier...")
			exit()
		try:
			userGuess = input("Your guess: ")
			hint = ""
		except:
			print("You must use a number!")
			print("This time, use a number (or type '" + Fore.YELLOW + "999" + Fore.RESET + "' to exit)")
			time.sleep(3)
			continue
		if userGuess == 999:
			print("Goodbye")
			exit()
		if userGuess == 888:
			print("Restarting...")
			time.sleep(2)
			restartMe()

		if userGuess == randomNumber:
			print("You got it!")
			time.sleep(1)
			found = True
		if userGuess > 100 or userGuess < 1:
			hint = hint + "You need to guess a number between 1 and 100!"
		elif userGuess > randomNumber:
			if userGuess > highGuess:
				hint = hint + "You went too high. "
			hint = hint + "Guess lower!"
			highGuess = userGuess
		else:
			if userGuess < lowGuess:
				hint = hint + "You went too low. "
			hint = hint + "Guess higher!"
			lowGuess = userGuess
		for x in userGuesses:
			if userGuess == x:
				hint = hint + " You already picked " + str(x) + "!"
				pass
		if highGuess-lowGuess == 2:
			hint = hint + " I bet you're going to guess " + str(highGuess-1) + " next."
		else:
			hint = hint + " Try " + str(int((round((highGuess-lowGuess)/2))+lowGuess)) + "."
		lastGuess = userGuess
		tries += 1
		userGuesses.append(userGuess)

	# Print congratulations and goodbye
	clearScreen()
	print("Thanks for playing our game!")
	print("You guessed " + str(tries) + " times.")
	allGuesses()

def checkFiles():
	# Check to see if game file has been modified while it is running.
	# If the file has been modified then restart.
	for f, mtime in WATCHED_FILES_MTIMES:
		if os.path.getmtime(f) != mtime:
			clearScreen()
			print("File modified.  Restarting game.")
			time.sleep(2)
			restartMe()

def numberLine():
	pass

def restartMe():
	os.execv(__file__, sys.argv)		# TODO: Set this in TRY block in case there is a permission failure here

def allGuesses():
	global userGuesses
	print("All guesses: "+ str(userGuesses))

def clearScreen():
	import subprocess as sp
	if platform.system() == "Darwin":
		tmp = sp.call('clear',shell=True)	# Use 'clear' method for OS X
	else:
		tmp = sp.call('cls',shell=True)		# Use 'cls' method for Windows (assuming non OS X is Windows)

def checkDependancies():
	for mod in sys.modules:				# TODO: Add list that contains depends. then loop through list
	# Make sys.modules a list, then compare to dependancies list
		if mod == "colorama":
			print("dependancies: Found colorama")
		if mod == "platform":
			print("dependancies: Found platform")
		if mod == "time":
			print("dependancies: Found time")
	time.sleep(2)

if __name__ == "__main__":
	main()
