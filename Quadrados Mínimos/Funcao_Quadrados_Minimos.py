# importa a biblioteca sympy para ser usada no código, essa biblioteca manipula expressões simbólicas
import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, Symbol
# importa a função init_printing da biblioteca sympy para melhorar a visualização das expressões simbólicas
from sympy import init_printing
# configura a função init_printing para melhorar a visualização das expressões simbólicas
init_printing(use_latex='png', scale=1.05, order='grlex',
              forecolor='Black', backcolor='White', fontsize=10)


# Define a função que calcula os coeficientes do polinômio de grau n que melhor se ajusta aos pontos (x, y) usando o método dos mínimos quadrados


def funcao_quadrados_minimos(x, y, n):
    # Converte as listas x e y em arrays numpy
    x = np.array(x)
    y = np.array(y)
    # Cria a matriz de Vandermonde para os valores de x, que é uma matriz onde cada linha é uma potência de x
    A = np.vander(x, n + 1)
    # Calcula os coeficientes do polinômio usando a fórmula dos mínimos quadrados: (A^T * A)^(-1) * A^T * y
    coeficientes = np.linalg.inv(A.T @ A) @ A.T @ y
    return coeficientes
