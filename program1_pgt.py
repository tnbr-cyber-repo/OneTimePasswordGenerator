#!usr/bin/env python3
# Cybersecurity Essentials
# Group Project - Password Guessing Tool
# Members: Tamika Burgess-Rose (A01075997)
#          Nimmy James
# -------------------------------------------
# Accept User Input
# Encrypt Input
# Compare against /etc/shadow
# Validate if Input exist in /etc/shadow

from colorama import Fore as Colors
from crypt import crypt
from os import getuid
from spwd import getspall, getspnam
from sys import argv


if getuid() != 0:
	print("You must be root user to run this utility.")
	exit(1)

if len(argv) <= 1:
	username = input("What user should we try to guess the password for? ")
	try:
		user = getspnam(username)[0]
	except:
		print(f"{username} not found")
		exit(1)
	finally:
		print(f"Attempt to guess password for {username}")
else:
	username = argv[1]

guess_password = input("Can you guess the password? ")
try:
	encrypted_password = getspnam(username)[1]

	guess_password = guess_password.rstrip()

	new_password = crypt(guess_password, encrypted_password)

except:
	print(f"{username} not found")
	exit(2)
else:
	print(f"Trying password:- {guess_password}....\n")
	# print(f"The /etc/shadow password for user is {encrypted_password}")
finally:
	if encrypted_password == new_password:
		print(Colors.LIGHTBLUE_EX + "Password found!\n" + Colors.RESET)
		print(f"The guessed password for user {username} is: {guess_password}")
		exit(1)
	else:
		print(Colors.RED + "Password NOT found!")

print(Colors.LIGHTYELLOW_EX + "Either Password entered did not match user or User entered did not match password. \n You're welcome to try again")

exit(1)


