numbers={'1':"Jeden",'2':"Dwa",'3':"Trzy",'4':"Cztery",'5':"Pięć",'6':"Sześć",
'7':"Siedem",'8':"Osiem",'9':"Dziewięć",'0':"Zero"}

string = input("Podaj ciąg cyfr do przekształcenia na string: ")
result = ''
for i in string:
    if i.isnumeric() == True:
        result += ' '+numbers[i]

print(result)