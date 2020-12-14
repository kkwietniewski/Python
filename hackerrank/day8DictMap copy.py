n = int(input())
phoneBook = {}
for i in range(n):
    name, phoneNumber = input().split()
    phoneBook[name] = phoneNumber
enterName = input()
while enterName:
    if enterName in phoneBook:
        print('{0}={1}'.format(enterName,phoneBook[enterName]))
    elif enterName not in phoneBook:
        print('Not found')
    enterName = input()