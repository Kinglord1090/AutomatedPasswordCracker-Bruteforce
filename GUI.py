import tkinter
from tkinter import *
import string
from itertools import product
window = Tk()
window.title("The Ultimate Bruteforcer"
def use():
  x = ["0", "1", "2", "3", "4", "5", "6", "7","8", "9", "A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "`", "~", "@", "#", "$", "&", "*", "(", ")", "%", "-", "+", "=", "/", ";", ":", "!", "?"  "€", "£", "¥", "_", "^", "[", "]", "{", "}", "§", "|", "~", "…", "\\", "<", ">", "'", "''", ",", ".", "₹"]
# X is the string which contains all the 101 characters of the keyboard!
  var = StringVar()
  entry = tkinter.Entry(window, textvariable=var)
# Y is the length of the passwords to be required!
# Z is the process which creates the list of passwords!
  def get():
    y = entry.get()
    z = [("".join(p)) for p in product(x, repeat=y)]
  submit = tkinter.Button(window, text='Submit', command=get
  for index in z:
    label=tkinter.Label(window, text='Click submit'
    label.config(text=str(index))
entry.pack()
submit.pack()
label.pack()

window.mainloop()
use()

