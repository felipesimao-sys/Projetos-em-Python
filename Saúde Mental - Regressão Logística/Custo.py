#Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import math
from GradienteDescendente import h

#Definindo a hipotese a função custo
def custo(x, y, a, b):
    m = len(x)
    custo_total = 0
    for i in range(m):
        custo_total += (h(x[i], b, a) - y[i])**2
    return custo_total/(m)
