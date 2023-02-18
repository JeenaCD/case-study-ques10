class Rectangle:
    def __init__(self, length ,breadth):
        self.length = length
        self.breadth = breadth 
    
    def Perimeter(self):
        return 2*(self.length + self.breadth)
    
    def Area(self):
        return self.length*self.breadth   
    