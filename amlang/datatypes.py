import parser
    
class function:
    
    def __init__(self, name, code):
        self.name = name
        self.code = code
        
        
class integer:
    
    def __init__(self, value):
        self.value = value
        self.string = str(value)
        
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
        
    def __mul__(self, other):
        return self.value * other.value
        
    def __div__(self, other):
        return self.value / other.value
        
    def __pow__(self, other):
        return self.value ** other.value
        
        
class string:
    
    def __init__(self, value):
        self.value = str(value)
        
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        raise Error
        
    def __mul__(self, other):
        return self.value * other.value
        
    def __div__(self, other):
        raise Error
        
    def __pow__(self, other):
        raise Error
