  
def hypotenuse(a, b):
  l = (a**2 + b**2)**0.5
  assert l >= 0 ("both a and b must be numerical")
  assert l > 0 ("both a and b must be greater than 0")
  return l

print (hypotenuse(4, 5))


