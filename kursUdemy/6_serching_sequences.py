numList = [2,3,4,5,6,8,9,5,6]


name = "arek"

#wyszukaj a w name
print('a' in name)
#true

print("Ilosc elementow: ",len(numList))

print("Najwiekszy element: ", max(numList))

print("Najmniejszy element: ", min(numList))

#funkcja list dzieli stringa na tablicę charów
charTab = list("metallica")
print(charTab,"\n")
print(len(charTab))

#slice and replace
charTab[5:] = " mania"
print(charTab,"\n")

charTab[5:] = list(" cure")
print(charTab,"\n")

#czyszczenie/usuwanie elementow
charTab[:6] = []
print(charTab,"\n")


