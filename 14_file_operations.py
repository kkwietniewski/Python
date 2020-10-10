file = open('c:/Users/Kacper/Desktop/qwe.txt', 'w')

file.write("Hello world!\n Hi\n Mama\n Third line")

file.close()

file = open('c:/Users/Kacper/Desktop/qwe.txt', 'r')
message = file.read()

print(message)
file.close()

file = open('c:/Users/Kacper/Desktop/qwe.txt', 'r')


message = file.read()

print(message)
message = file.readline()
print(message)

file.seek(0)

fileData = file.readlines()

print(fileData)

fileData[2] = "Second line\n"

file.close()

file = open('c:/Users/Kacper/Desktop/qwe.txt', 'w')

file.writelines(fileData)

file.close()

file = open('c:/Users/Kacper/Desktop/qwe.txt', 'r')

message = file.read()

print(message)