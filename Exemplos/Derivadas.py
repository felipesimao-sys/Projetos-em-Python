from sympy import diff, Symbol
from sympy import init_printing
init_printing(use_latex='png', scale=1.05, order='grlex',
              forecolor='Black', backcolor='White', fontsize=10)


x = Symbol('x')
e = Symbol('e')
y = Symbol('y')
f = 2*x**2 + y**3
#gradiente = [diff(f, x), diff(f, y)]
print(diff(f, x, y))


