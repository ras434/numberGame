#!/usr/bin/env python
import random, time, sys
from colorama import Fore
import os

userGuesses = []

WATCHED_FILES = [__file__]		# To add files to watch, create comma seperated list [file1, file2, file3]
WATCHED_FILES_MTIMES = [(f, os.path.getmtime(f)) for f in WATCHED_FILES]

def main():
	# Initialize the program
	global userGuesses
	clearScreen()
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
	os.execv(__file__, sys.argv)

def allGuesses():
	global userGuesses
	print("All guesses: "+ str(userGuesses))

def clearScreen():
	import subprocess as sp
	tmp = sp.call('clear',shell=True)

if __name__ == "__main__":
	main()
