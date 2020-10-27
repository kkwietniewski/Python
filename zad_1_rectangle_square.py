class Square:
    def calcSquareArea(self,x):
        return x*x

square = Square()
print(square.calcSquareArea(4))

class Rectangle(Square):
    def calcRectangleArea(self,x,y):
        return x*y
    
rectangle = Rectangle()
print("Pole kwadratu z dziecka klasy Rectangle: ",rectangle.calcSquareArea(6))
print("Pole prostokąta rodzica: ",rectangle.calcRectangleArea(6,5))