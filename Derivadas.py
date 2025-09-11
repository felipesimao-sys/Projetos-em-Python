from sympy import diff, Symbol
from sympy import init_printing
init_printing(use_latex='png', scale=1.05, order='grlex',
              forecolor='Black', backcolor='White', fontsize=10)


x = Symbol('x')
y = Symbol('y')
f = x**3+x*y+x**2+y**2
print(diff(f, x, y))
