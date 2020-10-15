def letter_shift(plaintext, key):
	bleh = "abcdefghijklmnopqrstuvwxyz"
	return bleh[(bleh.index(plaintext.lower()) + bleh.index(key.lower())) % 26]