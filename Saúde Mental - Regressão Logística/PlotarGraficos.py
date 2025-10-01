#importando as bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import math
from GradienteDescendente import h


#função para plotar os gráficos
def plotar_graficos(x, y, a, b):
    valores_x = [i for i in range(int(min(x))-1, int(max(x))+2)]
    valores_y = [h(x, b, a) for x in valores_x]
    plt.plot(valores_x, valores_y, 'r')
    plt.plot(x, y, 'bo')
    plt.show()