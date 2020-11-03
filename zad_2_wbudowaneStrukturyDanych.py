##Zadanie 1
#
#clist = [None]
#cities = ('Poznań', 'Warszawa','Gorzów WLKP', 'Kraków', 'Częstochowa')
#clist = list(cities)
##print(clist[-1])
#
#resultA = []
#resultB = []
#resultA = [ci for ci in clist if ci[0]>'K']
#print(resultA)
#
#resultB = [ci for ci in clist if len(ci)>6]
#print(resultB,'\n')
#
##Zadanie 2
#cal = {}
#c1={'1':"Styczeń",'2':"Luty",'3':"Marzec",'4':"Kwiecień",'5':"Maj",'6':"Czerwiec",'7':"Lipiec",'8':"Sierpień",'9':"Wrzesień",'10':"Październik",'11':"Listopad",'12':"Grudzień"}
#
#month = input("Podaj cyfrę miesiąca: ")
#print("Twój miesiąc to: ",c1[month],'\n')
#
##Zadanie 3
#a = {1,2,3,4,5}
#b = {1,7,8,3,10}
#
#print(a|b)
#print(a&b)
#print(a-b,'\n')
#
##Zadanie 4
#import math
#
#pi = math.pi
#r = float(input("Podaj r: "))
#def circle(pi,r):
#    l = 2*pi*r
#    pp = pi*r*r
#    tup = (l,pp)
#    return tup
#circle = circle(pi,r)
#
#print('Obwód koła: ',circle[0])
#print('Pole powierzchni: ',circle[1],'\n')

#Zadanie 5
path = 'text.txt'
i=0
while i!=2:
    line = str(input("Podaj ciąg do zapisania kończąc enterem: "))
    for l in line:
        if l == ' ':
            print('Koniec linii')
    i=i+1
#with open(path, 'w')as file:
#    file.writelines(x for x in open(path) if x!='z')
#    file.close()
#for c in userString:
#    if c == '\n':
#        print(c)