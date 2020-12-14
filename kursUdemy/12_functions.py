def simple(name):
	print('Function '+name)
	
simple('Nowa')

def gbp_to_usd(gbp):
	usd = gbp*1.5
	return usd
	
gbp = int(input('Type value of GBP: '))
usd = gbp_to_usd(gbp)
print('Value of USD: ',usd)


#deklaracja funkcji z nieokreśloną liczbą parametrów, magazynowanej w liście

def moreThanOneParameter(*param):
	print(param)
	
moreThanOneParameter('adadad',8,9,'diaiiaiaai',9,"paop")