# Part 2 of the Python Review lab.

def encode(x, y):
	if (1 < y < 250) and (500 < x < 1000):
		return( x * y)
	else:
		return("Invalid input: Outside range.")


def decode(coded_message):
	pass