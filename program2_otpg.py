#!/usr/bin/env python3

# Cybersecurity Essentials
# Group Project - Password Guessing Tool
# Student: Tamika Burgess-Rose (A01075997)
# -------------------------------------------
# Create One Time Password Generator
# Use Hexadecimal Key as Initialization Value
# Truncate hash to 6-digit Hexadecimal
# Generate and display the 1st 100 OTPs

import hashlib

passwords = []
key = '0810770FF00FF07012'

for x in range(0, 100):
    byte_key = bytes.fromhex(key)
    # print(byte_key)

    hash_key = hashlib.sha256(byte_key).hexdigest()
    key = hash_key
    otp = hash_key[:6]
    passwords.append(otp)
    # print(f"This is the hash_key Hex value: {hash_key}")

print("\nOne Time Password Generator\nBelow are 1st 100 generated")
for all_passwords in range(0, passwords.__len__()):
    print(f"{all_passwords + 1}: {passwords[all_passwords]}")
