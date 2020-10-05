import math

x = int(input("Value 1: "))
y = int(input("Value 2: "))
gcd = math.gcd(x,y)
lcm = str(x*y/gcd)

print("Najwiekszy wspolny dzielnik to: ",gcd)
print("Najwiekszy wspolna wielokrotnosc to: ",lcm)

