from sympy import *
from sympy import init_printing
init_printing() 
x = symbols('x')
expr = x**2
preview(expr, viewer='file', filename='output.png')