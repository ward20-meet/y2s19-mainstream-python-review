# Part 3 of the Python Review lab.

LETTERS_TO_NUMBERS = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11,
					  'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22,
					  'x':23, 'y':24, 'z':25}

NUMBERS_TO_LETTERS = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l',
					  12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w',
					  23: 'x', 24: 'y', 25: 'z'}

def createShiftDictionary(s):
	d={}
	for letter in LETTERS_TO_NUMBERS:
		index = LETTERS_TO_NUMBERS[letter] + s
		index = index % 26
		d[letter] = NUMBERS_TO_LETTERS[index]
	return(d)


def encode(plaintext, s):
	mytext= ""
	for letter in plaintext:
		if letter in createShiftDictionary(s):
			mytext += createShiftDictionary(s)[letter] 
		else:
			mytext+=letter
	print(mytext)
	return(mytext)



def decode(ciphertext, s):
	yourtext=""
	for letter in ciphertext:
		yourtext = createShiftDictionary[letter] - s

	print(yourtext)
	return(yourtext)




def decodeAll(ciphertext):
	pass



encode("hi my name is ward",3)
decode("hi my name is ward",3)







