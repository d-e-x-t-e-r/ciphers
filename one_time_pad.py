"""
One-time Pad cipher that encrypts a message by shifting each of the content
letters a certain randomly-generated amount.

The settings for the message are in the Main function.

Created by Dexter.
Python 3.6
"""

import string
import secrets

def encrypt(message, shift):
	encryption = ""
	counter = 0

	for i in message:
		for j in string.ascii_uppercase:
			if i == j:
				# Finds index of matching letter in alphabet.
				mes_ind = string.ascii_uppercase.find(i)

				# Ensures proper wrap around.
				if mes_ind + shift[counter] > 25:
					mes_ind -= 26

				# Encrypts.
				enc_letter = string.ascii_uppercase[mes_ind+shift[counter]]
				encryption += enc_letter

				# Increments counter.
				counter += 1

	return encryption

def decrypt(encryption, shift):
	# New shift list to get back to original value.
	dec_shift = []
	for i in range(len(shift)):
		dec_shift.append(26 - shift[i])

	# We can use the encrypt function with the new shift to decrypt.
	decryption = encrypt(encryption, dec_shift)

	return decryption

def Main():
	print("Welcome to the One Time Pad Cipher.\n")

	##### SETTINGS ######

	# Input the message you would like encypted.
	message = "Thanks for taking a look at my one time pad cipher!"

	##### END SETTINGS #####

	# Removes punctuation, whitespace, and numbers from the message.
	# This should make it harder for someone to decode, but the message should
	# remain understandable when decrypted.
	# In this case, I've removed each of these things to make the message
	# essentially impossible to decode without the key.
	# Numbers should be written in their word form, otherwise they will be 
	# removed. (or you could make a simple converter if you liked)
	non_letters = string.punctuation + string.whitespace + string.digits
	table = str.maketrans({key: None for key in non_letters})
	message = message.translate(table)

	# Gets shift values from random generation and stores them in a list.
	# The shift is exactly as long as the message.
	shift = []
	for i in range(len(message)):
		shift.append(secrets.randbelow(27))

	print("Shifting the input by this list:", shift)

	# Calling encryption function.
	# For aesthetic purposes and simplicity, we make the message uppercase only.
	encryption = encrypt(message.upper(), shift)
		
	print("\nYour encrypted message is:\n", encryption, sep="")

	# Calling decryption function.
	decryption = decrypt(encryption, shift)

	print("Your decrypted message is:\n", decryption, sep="")

Main()
