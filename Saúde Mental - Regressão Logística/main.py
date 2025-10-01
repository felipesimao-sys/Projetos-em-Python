# Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import math
from PlotarGraficos import plotar_graficos
from GradienteDescendente import h

# definindo os dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# definindo taxa de aprendizado
t = 0.001

# definindo o valor inicial para a e b
a = 0.1
b = 0.1

# Plotando o gráfico inicial
plotar_graficos(x, y, a, b)
