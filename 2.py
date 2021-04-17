
# Import sympy
from sympy import * 
from sympy import init_printing
  
# Define symbols and trigo expression
x, y = symbols('x y')
gfg = Integral(sqrt(1 / x), x)
  
print(gfg)