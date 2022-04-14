  
def hypotenuse(a, b):
   h = (a**2 + b**2)**0.5
   return h

def is_numeric(n):
    if isinstance(n, int):
        assert n > 0, "Both a and b must be numeric"
        return True
      
    if isinstance(n, float):
        return n.is_integer()
    return False

  