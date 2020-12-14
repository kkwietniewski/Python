far = []
def getFahrenheit(c):
    f = round(c*(9/5)+32,2)
    if c >0:
        sign = '+'+str(c)+' stopni Celsjusza to: '+str(f)+' stopni Fahrenheita'
    else:
        sign = str(c)+' stopni Celsjusza to: '+str(f)+' stopni Fahrenheita'
    return sign


for c in range(-20,45,5):
    far.append(getFahrenheit(c))
for f in far:
    print(f)