"""
Caesar cipher that encrypts a message by shifting the content letters by a 
chosen amount. 

The settings for the shift amount and message are in the Main function.

Created by Dexter.
Python 3.6
"""

import string
import math

def encrypt(message, shift):
	encryption = ""

	for i in message:
		for j in string.ascii_uppercase:
			if i == j:
				# Finds index of matching letter in alphabet.
				mes_ind = string.ascii_uppercase.find(i)

				# Ensures proper wrap around.
				if mes_ind + shift > 25:
					mes_ind -= 26

				# Encrypts.
				enc_letter = string.ascii_uppercase[mes_ind+shift]
				encryption += enc_letter

		for k in string.digits:
			if i == k:
				# Copies number to string.
				encryption += string.digits[int(i)]

		for w in string.whitespace:
			if i == w:
				# Copies whitespace.
				mes_ind = string.whitespace.find(i)
				encryption += string.whitespace[mes_ind]

	return encryption

def decrypt(encryption, shift):
	# New shift to get back to original value.
	dec_shift = 26 - shift

	# We can use the encrypt function with the new shift to decrypt.
	decryption = encrypt(encryption, dec_shift)

	return decryption

def Main():
	print("Welcome to the Caesar Cipher.\n")

	##### SETTINGS ######

	# Choose the amount that you would like to shift by.
	shift = 13
	# Input the message you would like encypted.
	message = "Thanks for taking a look at my Caesar cipher!"

	##### END SETTINGS #####

	# Ensures positive integer value.
	shift = math.floor(math.fabs(shift))

	# Getting our shift value to be between 0 and 26.
	if shift > 26:
		shift = shift - 26 * (shift // 26)

	# Removes punctuation from the message.
	# This should make it harder for someone to decode, but the message should
	# remain understandable when decrypted.
	table = str.maketrans({key: None for key in string.punctuation})
	message = message.translate(table)

	print("Shifting the input by this many letters:", shift)
	print("Message to be encrypted:\n", message, sep="")

	# Calling encryption function.
	# For aesthetic purposes and simplicity, we make the message uppercase only.
	encryption = encrypt(message.upper(), shift)
		
	print("\nYour encrypted message is:\n", encryption, sep="")

	# Calling decryption function.
	decryption = decrypt(encryption, shift)

	print("Your decrypted message is:\n", decryption, sep="")

Main()
