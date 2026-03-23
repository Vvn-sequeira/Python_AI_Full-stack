
class Rectangle():
    def __init__(self , l , w):
        self.l =l 
        self.w = w 
        
    def area(self): 
        return self.l * self.w 
    
    def perimeter(self): 
        return (2*(self.l+self.w))
    
class Box(Rectangle):
    def __init__(self, l, w , h):
        super().__init__(l, w)
        self.h = h 
        
    def Vlume(self):
        return l *w * self.h
        
    def area(self):
        return 2*(l * w + l * self.h + w * self.h )
        
    def Display(self):
        print(f"Area of an Rectangle : {super().area()}")
        print(f"Perimeter of a Rectangle : {super().perimeter()}")
        print(f"Vlume of the Box : {self.Vlume()}")
        print(f"Area of the Box : {self.area()}")
        
        
l , w , h = map(int , input("Enter L | w | H ").split())

b = Box(l , w , h)
b.Display() 
