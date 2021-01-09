#Password Generator Project
import string
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
l_password = ""
s_password = ""
n_password = ""

for letter in range(nr_letters):
  l_password += random.choice(letters)

for symbol in range(nr_symbols):
  s_password += random.choice(symbols)

for number in range(nr_numbers):
  n_password += random.choice(numbers)

final_pass = str(l_password) + str(s_password) + str(n_password)

l = list(final_pass)
random.shuffle(l)
final_pass = ''.join(l)

print(f"Here is your password {final_pass}")