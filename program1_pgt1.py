#!usr/bin/env python3
# Cybersecurity Essentials
# Group Project - Password Guessing Tool
# Student: Tamika Burgess-Rose (A01075997)
# -------------------------------------------
# Accept User Input
# Encrypt Input
# Compare against /etc/shadow
# Validate if Input exist in /etc/shadow

from colorama import Fore as Colors
from crypt import crypt
from os import getuid
from spwd import getspnam
from sys import argv

def main():
	new_password = ""
	encrypted_password = ""

	if getuid() != 0:
		print("You must be root user to run this utility.")
		exit(1)

	if len(argv) <= 1:
		username = input("Enter Username: ").lower()
		try:
			username = getspnam(username)[0]
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

		if encrypted_password == '*' or encrypted_password == '!':
			print('No password detected')
			exit(1)
		else:
			guess_password = guess_password.rstrip()

			new_password = crypt(guess_password, encrypted_password)

	except:
		print(f"Password for {username} not found")
		exit(1)
	else:
		print(f"Trying password:- {guess_password}....\n")
	finally:
		if encrypted_password == new_password:
			print(Colors.LIGHTBLUE_EX + "Password found!\n" + Colors.RESET)
			print(f"The guessed password for user {username} is: {guess_password}\n")
			exit(0)
		else:
			print(Colors.RED + "Password NOT found!")

		print(
			Colors.LIGHTYELLOW_EX + "Either Password entered did not match user or User entered did not match password. "
									"\n You're welcome to try again\n")

	exit(1)

if __name__ == '__main__':
	main()

