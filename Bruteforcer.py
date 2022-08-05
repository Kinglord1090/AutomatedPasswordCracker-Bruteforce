from itertools import product
import time

characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "`", "~", "@", "#", "$", "&", "*", "…", "\\", "<", ">", "'", ",", ".", "₹"]
# characters is a list which contains 100 characters from the keyboard

while True:
	try:
		min_length = int(input("Enter the minimum length of the passwords to be generated: "))
		break
	except ValueError:
		print("Enter a valid number!!")
min_length -= 1
# min_length is the minimum length of the passwords to be generated

while True:
	try:
		max_length = int(input("Enter the maximum length of the passwords to be generated: "))
		break
	except ValueError:
		print("Enter a valid number!!")
# max_length is the maximum length of the passwords to be generated

guess = None            # guess is the guessed combination which is used later at line 42
password = "1234"          # password is a sample string used for testing
start_time = time.time()     # start_time is the start point of time
no_of_guesses = 0               # no_of_guesses is an int value thats incremented at each loop to know the number of guesses tried out by the code


def use():
	if min_length < max_length:
		min_length += 1
		for x in product(a, repeat=b):    # x is the raw form of the combination
			guess = "".join(x)
			if guess != password:
				print(guess)
				no_of_guesses += 1
			else:
				stop_time = time.time()           # stop_time is the stop point of time
				time_taken = stop_time - start_time                 # J is the total time taken!
				try:
					print("\nPassword Found!!\nThe password is: " + guess + "\nTried out " + str(no_of_guesses) +
					      " possible passwords in " + str(time_taken) + " seconds!!\nThat is " + str(no_of_guesses / time_taken) +
					      " passwords per second!!")
					break
				except ZeroDivisionError:
					print("\nPassword Found!!\nThe password is: " + guess + "\nTried out " + str(no_of_guesses) +
					      " possible passwords in " + str(time_taken) + " seconds!!\nThat is " + str(no_of_guesses / time_taken) +
					      " password guesses in less than a second!!")
					break
		for y in range(min_length):
			if guess != password:
				use()
			else:
				break


if __name__ == "__main__":
	use()
