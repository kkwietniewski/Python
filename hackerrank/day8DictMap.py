n = int(input())
phoneBook = {}
for i in range(n):
    name, phoneNumber = input().split()
    phoneBook[name] = phoneNumber
while True:
    try:
        enterName = input()
        phoneNumber = phoneBook.get(enterName)
        if phoneNumber:
            print('{0}={1}'.format(enterName,str(phoneBook[enterName])))
        else:
            print('Not found')
    except:
        break