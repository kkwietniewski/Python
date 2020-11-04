#Zadanie 1

clist = [None]
cities = ('Poznań', 'Warszawa','Gorzów WLKP', 'Kraków', 'Częstochowa')
clist = list(cities)
#print(clist[-1])

resultA = []
resultB = []
resultA = [ci for ci in clist if ci[0]>'K']
print(resultA)

resultB = [ci for ci in clist if len(ci)>6]
print(resultB,'\n')

#Zadanie 2
cal = {}
c1={'1':"Styczeń",'2':"Luty",'3':"Marzec",'4':"Kwiecień",'5':"Maj",'6':"Czerwiec",'7':"Lipiec",'8':"Sierpień",'9':"Wrzesień",'10':"Październik",'11':"Listopad",'12':"Grudzień"}

month = input("Podaj cyfrę miesiąca: ")
print("Twój miesiąc to: ",c1[month],'\n')

#Zadanie 3
a = {1,2,3,4,5}
b = {1,7,8,3,10}

print(a|b)
print(a&b)
print(a-b,'\n')

#Zadanie 4
import math

pi = math.pi
r = float(input("Podaj r: "))
def circle(pi,r):
    l = 2*pi*r
    pp = pi*r*r
    tup = (l,pp)
    return tup
circle = circle(pi,r)

print('Obwód koła: ',circle[0])
print('Pole powierzchni: ',circle[1],'\n')

#Zadanie 5
path = 'text.txt'
line = str(input("Podaj ciąg do zapisania kończąc enterem: "))
with open(path,'a') as file:
    file.write(line)
    while line.strip():
        line = str(input("Podaj ciąg do zapisania kończąc enterem: "))
        file.write(line)
    file.close()
    
#Zadanie 6
pathP = 'people.txt'
i = 1
name = ' '
lastName = ' '
year = 0
end = False

while end != True: 
    name = str(input("Podaj imię: "))
    lastName = str(input("Podaj nazwisko: "))
    year = input("Podaj rok urodzenia: ")
    if name == '' or lastName == '' or year == '':
        print("Nie podałeś danych, wyświetlić plik?\n")
        print("[Tak],[Any key or sentence] - Nie\n")
        answer = str(input())
        if answer == 'Tak' or answer == 'tak':
            with open(pathP) as file:
                lines = file.readlines()
            print(lines)
        else:
            end = True
    else:
        age = str(2020 - int(year))
        with open(pathP,'a+') as file:
            output = str(i),". Imię: ",name,", Nazwisko: ",lastName,", Wiek: ",age,'\n'
            file.writelines(o for o in output if o != '')
            file.close()
            i=i+1