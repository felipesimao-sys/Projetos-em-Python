#Recebe a matriz M, o vetor x e o vetor c e retorna o vetor gradiente g
from vetor_gradiente import vetor_gradiente
import numpy as np
dados = [[0,10], [2,9], [4,7], [6,5], [8,3], [10,0]]
xdados = [i[0] for i in dados]
ydados = [i[1] for i in dados]


#lê o grau do polinômio
n = int(input("Digite o grau do polinômio: "))
A = np.vander(xdados, n+1)

M = A.T @ A
c = A.T @ ydados
x = np.zeros(n+1)
t = 10**(-5.5)
i=0
while i<1000000:
    g = vetor_gradiente(M, x, c)
    x = x - t*g
    i=i+1
    #print("Iteração:", i, "Valor do gradiente:", g, "Valor de x:", x)



print("Os valor dos coeficientes:", x)

