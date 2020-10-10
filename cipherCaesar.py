wordToConvert = input("Type word to convert: ")
key = int(input("Type value of key: "))

print("\nTyped word: "+wordToConvert)

encrypted = ""

for i in range(len(wordToConvert)):
	if ord(wordToConvert[i]) == 32:
		encrypted += wordToConvert[i]
	elif ord(wordToConvert[i]) > 122 - key:
		encrypted += chr(ord(wordToConvert[i]) + key - 26)
	else:
		encrypted += chr(ord(wordToConvert[i]) + key)
		
print("Encrypted word: "+encrypted)

#range() metoda wyznaczająca liczby od 0 do podanej
#ord() metoda wyznaczająca numer dla podanej litery z tablicy ASCII
#chr() metoda odwrotna dla ord(), wyznacza literę na podstaie numeru z tablicy ASCII
#elif == else if