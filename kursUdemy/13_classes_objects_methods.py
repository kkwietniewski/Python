class calculator:
	def add(self,x,y):
		return x+y
	def sub(self,x,y):
		return x-y

calc = calculator()

resAdd = calc.add(4,50)
resSub = calc.sub(10,11)

print('Add: ',resAdd, 'Sub: ', resSub)

#rozszerzenie klasy

class class1:
	value1 = 'Value from class1'
	
class class2:
	value2 = 'Value from class2'
	
class class3(class1, class2):
	value3 = 'Value from class3'
	
show = class3()

print('\n')
			
print(show.value1)
print(show.value2)
print(show.value3)