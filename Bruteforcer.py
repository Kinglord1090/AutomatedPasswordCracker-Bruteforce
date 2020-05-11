import string
from itertools import product

def use():
  x = ["0", "1", "2", "3", "4", "5", "6", "7","8", "9", "A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "`", "~", "@", "#", "$", "&", "*", "(", ")", "%", "-", "+", "=", "/", ";", ":", "!", "?"  "€", "£", "¥", "_", "^", "[", "]", "{", "}", "§", "|", "~", "…", "\\", "<", ">", "'", "''", ",", ".", "₹"]
# X is the string which contains all the 101 characters of the keyboard!
  y = int(input("Length: "))
# Y is the length of the passwords to be required!
  z = [("".join(p)) for p in product(x, repeat=y)]
# Z is the process which creates the list of passwords!
  for index in z:
    print(index)
    command = input("Enter E to End program ->")
    if "e" in command:
      from blessings import Terminal
      t = Terminal()
      print(t.red("Exiting..."))
      break
      


use()
