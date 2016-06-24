import random

def greeting():
	print("Welcome to the Number Guess Game!")
	print("You have 5 chances to correctly guess the number the computer is thinking of. \nGood luck!")

def game():
	guess_count = 5
	while(guess_count):
		try:
			guess = int(input("Guess a number between 1 and 100: "))
		except NameError:
			print("That's not a number, please try again!")
		except SyntaxError:
			print("That's not a number, please try again!")
		else:
			if guess == computer_number:
				print("\nCongrats! You guessed correctly! The computer's number was {}".format(computer_number))
				break
					
			elif guess < computer_number:
				print("\vSorry, your guess was too low!")
				print("You have {} guesses left".format(guess_count - 1))
					
			elif guess > computer_number:
				print("\nDarn, that guess is too high!")
				print("You have {} guesses left".format(guess_count - 1))

			guess_count -= 1

	if guess_count == 0:
		print("Sorry, you're out of guesses! The computer's number was {}".format(computer_number))

computer_number = random.randint(0, 101)

greeting()
game()

play_again = raw_input("\nWould you like to play again? Type 'yes' or 'no' : ")
if play_again == "yes":
	game()
elif play_again == "no":
	print("\nThanks for playing!")
else:
	print("Please type 'yes' or 'no")

	