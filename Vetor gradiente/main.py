# Recebe a matriz M, o vetor x e o vetor c e retorna o vetor gradiente g
from vetor_gradiente import vetor_gradiente
import numpy as np
import time
dados = [[0, 10], [2, 9], [4, 7], [6, 5], [8, 3], [10, 0]]
xdados = [i[0] for i in dados]
ydados = [i[1] for i in dados]


# lê o grau do polinômio
n = int(input("Digite o grau do polinômio: "))
A = np.vander(xdados, n+1)

# liga um cronômetro para mostrar tempo de execução
inicio = time.time()


M = A.T @ A
c = A.T @ ydados
x = np.zeros(n+1)
t = 10**(-5.5)
i = 0
while i < 100000000:
    g = vetor_gradiente(M, x, c)
    x = x - t*g
    i = i+1
    print("Iteração:", i, "Valor do gradiente:", g, "Valor de x:", x)

fim = time.time()
print("Tempo de execução:", fim-inicio, "segundos")

print("Os valor dos coeficientes:", x)
