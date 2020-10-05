word = input("Enter word to search for letter: ")

print("Your word: " + word)

letter = input("Enter letter to search: ")

if(letter in word):
	#true
	print("Letter found, it's '"+letter+"'.")
else:
	#false
	print("Letter not found!")