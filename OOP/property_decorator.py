# @property = Decorator used to define a method as a property (it can be acessed like an attirbute)
#           Benefit: Add Additional logic when read, write or delete attributes
#           Gives you getter, setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return f"{self._width:.1f} cm"
    
    @property
    def height(self):
        f"{self._height:.2f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be great than zero")    
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be great than zero")    

    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
        
        
rec1 = Rectangle(5,2.5)
rec1.height = 10 #setting new values to the attirbutes
rec1.width = 25


del rec1.width #deleting value from the attributes
print(rec1.height)
print(rec1.width)