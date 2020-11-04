from itertools import product
import time

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "`", "~", "@", "#", "$", "&", "*", "…", "\\", "<", ">", "'", ",", ".", "₹"]
# A is the array which contains all 100 characters of the keyboard!

while True:
	try:
		b = int(input("Enter the minimum length of the passwords to be generated: "))
		break
	except ValueError:
		print("Enter a valid number!!")
b -= 1
# B is the minimum length of the passwords to be generated!

while True:
	try:
		c = int(input("Enter the maximum length of the passwords to be generated: "))
		break
	except ValueError:
		print("Enter a valid number!!")
# C is the maximum length of the passwords to be generated!

d = None            # D is the guessed password which is used later at line 42!
e = "1234"          # E is a sample password. Change it according to your desire!
f = time.time()     # F is the start point of time!
g = 0               # G is the number of guesses tried out by the code!


def use():
	global b, d, e, g
	if b < c:
		b += 1
		for h in product(a, repeat=b):    # H is the raw form of the guessed password(d)!
			d = "".join(h)
			if e != d:
				print(d)
				g += 1
			elif e == d:
				i = time.time()           # I is the stop point of time!
				j = i - f                 # J is the total time taken!
				try:
					print("\nPassword Found!!\nThe password is: " + d + "\nTried out " + str(int(g)) +
					      " possible passwords in " + str(int(j)) + " seconds!!\nThat is " + str(int(g) / int(j)) +
					      " passwords per second!!")
					break
				except ZeroDivisionError:
					print("\nPassword Found!!\nThe password is: " + d + "\nTried out " + str(int(g)) +
					      " possible passwords in " + str(int(j)) + " seconds!!\nThat is " + str(int(g)) +
					      " password guesses in less than a second!!")
					break
		for k in range(b):
			if e != d:
				use()
			elif e == d:
				break


use()
