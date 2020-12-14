pesel = ''
while pesel == '':
    tmp = input('Type pesel(11 num): ')
    if tmp.isnumeric() == True and len(tmp) == 11:
        pesel = tmp
    else:
        print('Incorrect pesel number(Must be 11 numbers')
# 98 07 01 0177 4
# pesel = '98070101774'
weight = [1,3,7,9]
numberSum = []
for i in range(len(pesel)):
    if i == 0 or i == 4 or i == 8:
        numberSum.append(int(pesel[i])*weight[0])
    elif i == 1 or i == 5 or i == 9:
        numberSum.append(int(pesel[i])*weight[1])
    elif i == 2 or i == 6:
        numberSum.append(int(pesel[i])*weight[2])
    elif i == 3 or i == 7:
        numberSum.append(int(pesel[i])*weight[3])
# print(numberSum)
lastNumber = str(sum(numberSum))
lastNumber = lastNumber[-1]
# print(lastNumber)
operationResult = 10-int(lastNumber)
# print(operationResult)
if operationResult == int(pesel[-1]):
    print('Your typed pesel is valid')
else:
    print('Your typed pesel is not valid')