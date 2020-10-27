fibNumber = int(input("Podaj n-ty wyraz ciągu Fibonacciego do wyświetlenia: "))

i=1
a=0
b=1
while i <= fibNumber:
    b = b+a
    a = b-a
    if i == fibNumber:
        print("Twoj wyraz ciagu Fibonaccieg: ", a)
    i=i+1