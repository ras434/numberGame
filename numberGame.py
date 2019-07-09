#!/usr/bin/env python
import random
import time
import sys
import platform
import curses
from colorama import Fore
import os

user_guesses = []

WATCHED_FILES = [__file__]		# To add files to watch, create comma separated list [file1, file2, file3]
WATCHED_FILES_MTIMES = [(f, os.path.getmtime(f)) for f in WATCHED_FILES]


def main():
	# Initialize the program

	# Check dependencies

	# Determine if running under Windows OS

	# Determine if colorama is available

	# Install any Windows specific requirements, if needed

	global user_guesses, last_guess
	check_dependencies()
	# clearScreen()  # might not need this function due to curses features
	my_screen = curses.initscr()
	my_screen.border(0)
	my_screen.addstr(12, 25, "numberGame.py")
	my_screen.refresh()
	# my_screen.getch()
	time.sleep(1)
	curses.endwin()
	print("Guess a number between 1 and 100.")
	time.sleep(1)
	print("Type '" + Fore.YELLOW + "999" + Fore.RESET + "' to exit game.")
	time.sleep(1)
	# random_number = 35
	tries = 0
	random_number = random.randint(1, 100)
	found = False  # flag variable to see if they guessed it
	hint = ""
	user_guess = 0
	last_guess = 0
	high_guess = 100
	low_guess = 1

# Run through the guessing process
	while not found:
		clear_screen()
		check_files()
		print("Tries: [" + str(tries) + "]\nGuess a number between " + str(low_guess) + " and " + str(high_guess))
		if len(user_guesses) > 0:
			print("Last guess: " + str(user_guess) + ", " + hint)
			all_guesses()  # Display all Guesses
		else:
			print("\n")
		if len(user_guesses) > 15:
			import subprocess as sp
			_ = sp.call('say you should probably try something easier', shell=True)
			print("You should probably try something easier...")
			exit()
		user_guess = input("Your guess: ")
		hint = ""
		if user_guess.isalpha():
			print("You must use a number!")
			print("This time, use a number (or type '" + Fore.YELLOW + "999" + Fore.RESET + "' to exit)")
			time.sleep(3)
			continue
		if user_guess == 999:
			print("Goodbye")
			exit()
		if user_guess == 888:
			print("Restarting...")
			time.sleep(2)
			restart_me()
		if user_guess == random_number:
			print("You got it!")
			time.sleep(1)
			found = True
		if user_guess > high_guess or user_guess < low_guess:
			hint = hint + "You need to guess a number between {} and {}!".format(low_guess, high_guess)
		elif user_guess > random_number:
			if user_guess > high_guess:
				hint = hint + "You went too high. "
			hint = hint + "Guess lower!"
			high_guess = user_guess
		else:
			if user_guess < low_guess:
				hint = hint + "You went too low. "
			hint = hint + "Guess higher!"
			low_guess = user_guess
		for x in user_guesses:
			if user_guess == x:
				hint = hint + " You already picked " + str(x) + "!"
				pass
		if high_guess-low_guess == 2:
			hint = hint + " I bet you're going to guess " + str(high_guess-1) + " next."
		else:
			hint = hint + " Try " + str(int((round((high_guess-low_guess)/2))+low_guess)) + "."
		last_guess = user_guess
		tries += 1
		user_guesses.append(user_guess)

	# Print congratulations and goodbye
	clear_screen()
	print("Thanks for playing our game!")
	print("You guessed " + str(tries) + " times.")
	all_guesses()


def check_files():
	# Check to see if game file has been modified while it is running.
	# If the file has been modified then restart.
	for f, minute_time in WATCHED_FILES_MTIMES:
		if os.path.getmtime(f) != minute_time:
			clear_screen()
			print("File modified.  Restarting game.")
			time.sleep(2)
			restart_me()


def number_line():
	pass


def restart_me():
	os.execv(__file__, sys.argv)  # TODO: Set this in TRY block in case there is a permission failure here


def all_guesses():
	global user_guesses
	print("All guesses: " + str(user_guesses))


def clear_screen():
	import subprocess as sp
	if platform.system() == "Darwin":
		_ = sp.call('clear', shell=True)  # Use 'clear' method for OS X
	else:
		_ = sp.call('cls', shell=True)  # Use 'cls' method for Windows (assuming non OS X is Windows)


def check_dependencies():
	for mod in sys.modules:  # TODO: Add list that contains depends. then loop through list
		# Make sys.modules a list, then compare to dependencies list
		if mod == "colorama":
			print("dependencies: Found colorama")
		if mod == "platform":
			print("dependencies: Found platform")
		if mod == "time":
			print("dependencies: Found time")
	time.sleep(2)


if __name__ == "__main__":
	main()
