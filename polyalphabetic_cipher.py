"""
Polyalphabetic cipher that encrypts a message by shifting the content letters an
amount given by a word.

Ex: Shift by DEXTER
D = 4, E = 5, X = 24, T = 20, E = 5, R = 18
So the cipher would shift the first letter by 4, second by 5, etc.
After the word is finished, you simply repeat the process.
Note: Whitespace is skipped over.

The settings for the shift word and message are in the Main function.

Created by Dexter.
Python 3.6
"""

import string

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

				# Increments counter and restarts it when necessary.
				counter += 1
				if counter >= len(shift):
					counter = 0


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
	# New shift list to get back to original value.
	dec_shift = []
	for i in range(len(shift)):
		dec_shift.append(26 - shift[i])

	# We can use the encrypt function with the new shift to decrypt.
	decryption = encrypt(encryption, dec_shift)

	return decryption

def Main():
	print("Welcome to the Polyalphabetic Cipher.\n")

	##### SETTINGS ######

	# Input the word that you would like to use as a shift.
	# Longer words are stronger ciphers.
	# Note: Sentences are also acceptable.
	shift_word = "encrypt"
	# Input the message you would like encypted.
	message = "Thanks for taking a look at my polyalphabetic cipher!"

	##### END SETTINGS #####

	# Removes non-letters (punctuation, whitespace, and digits) from shift_word.
	non_letters = string.punctuation + string.whitespace + string.digits
	non_letters_table = str.maketrans({key: None for key in non_letters})
	shift_word = shift_word.translate(non_letters_table)

	# Gets shift values from shift word and stores them in a list.
	shift = []
	for i in shift_word.upper():
		for j in string.ascii_uppercase:
			if i == j:
				shift_index = string.ascii_uppercase.find(i)
				shift.append(shift_index + 1)

	# Removes punctuation from the message.
	# This should make it harder for someone to decode, but the message should
	# remain understandable when decrypted.
	p_table = str.maketrans({key: None for key in string.punctuation})
	message = message.translate(p_table)

	print("Shifting the input by this list:", shift)
	print("Message to be encrypted:\n", message, sep="")

	# Calling encryption function.
	# For aesthetic purposes and simplicity, we make the message uppercase only.
	encryption = encrypt(message.upper(), shift)
		
	print("\nYour encrypted message is:\n", encryption, sep="")

	# Calling decryption function.
	decryption = decrypt(encryption, shift)

	print("Your decrypted message is:\n", decryption, sep="")

Main()
