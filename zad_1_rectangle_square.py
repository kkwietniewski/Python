class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calcArea(self):
        return self.x*self.y
			
class Square(Rectangle):
    def __init__(self,x):
        self.x = x
        self.y = x
        
rectangle= Rectangle(6,5)
square= Square(6)
print("Pole kwadratu z dziecka klasy Rectangle: ",square.calcArea())
print("Pole prostokąta rodzica: ",rectangle.calcArea())