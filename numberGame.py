#!/usr/bin/env python
import random, time

userGuesses = []

def main():
	# Initialize the program
	global userGuesses
	print("Guess a number between 1 and 100.")
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
		print("Guesses: " + str(tries) + " l: " + str(lowGuess) + " h: " + str(highGuess))
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
			hint = "This time, use a number (or type '999' to exit)"
			time.sleep(1)
			continue
		if userGuess == 999:
			print("Goodbye")
			exit()
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

def numberLine():
	pass

def allGuesses():
	global userGuesses
	print("All guesses: "+ str(userGuesses))

def clearScreen():
	import subprocess as sp
	tmp = sp.call('clear',shell=True)

if __name__ == "__main__":
	main()
