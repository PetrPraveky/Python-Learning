from sympy import *
from sympy import init_printing
init_printing() 
y, x = symbols("y x")
expr = parse_expr("-1/12")
preview(expr, viewer='file', filename='output.png')