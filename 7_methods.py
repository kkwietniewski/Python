words = ['graphic', 'processor', 'speaker', 'motherboard', 'cd-rom']
print(words,"\n")

#dodaje na koniec nowy element
words.append('mouse')
print(words,"\n")

numbers = [5,6,5,3,2,2,2,2,5,5,4,8,5]
#metoda count liczy ilość wystapienia wyszukiwanego elementu w tablicy i zwraca tą ilość 
print(numbers.count(5))

#rozszerzenie listy numbers po przez konkatenację
#numbers = numbers + words

#rozszerzenie po przez metodę extend
numbers.extend(words)
print(numbers)