import winsound
from time import sleep

MorseDictionary = {
	"a": ".-",
	"b": "-...",
	"c": "-.-.",
	"d": "-..",
	"e": ".",
	"f": "..-.",
	"g": "--.",
	"h": "....",
	"i": "..",
	"j": ".---",
	"k": "-.-",
	"l": ".-..",
	"m": "--",
	"n": "-.",
	"o": "---",
	"p": ".--.",
	"q": "--.-",
	"r": ".-.",
	"s": "...",
	"t": "-",
	"u": "..-",
	"v": "...-",
	"w": ".--",
	"x": "-..-",
	"y": "-.--",
	"z": "--..",
}

FREQUENCY = 1350

DotLength = 111
DashLength = 333

while True:
	print("type a message to translate to morse code:")
	inputMessage = input()
	inputMessage = inputMessage.lower()
	outputString = ""
	codedString = ""
	for char in inputMessage:
		if char != " ":
			code = MorseDictionary[char]
			outputString += code
			outputString += " "
			for morse in code:
				codedString += morse
			codedString += "00"
		else:
			codedString += "0000000"

	print(outputString)
	for code in codedString:
		if code == ".":
			winsound.Beep(FREQUENCY, DotLength)
			sleep(0.1)
		elif code == "-":
			winsound.Beep(FREQUENCY, DashLength)
			sleep(0.1)
		elif code == "0":
			sleep(float(DotLength) / 1000)