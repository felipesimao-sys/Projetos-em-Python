#para intalar o pacote para trabalhar com matrizes usar o comando
# pip install numpy


#importa a biblioteca numpy para ser usada no código, essa biblioteca manipula matrizes
import numpy as np
#importa a biblioteca matplotlib para ser usada no código, essa biblioteca cria os gráficos
import matplotlib.pyplot as plt

#atribui a matriz_a 3x3
matriz_a = np.array([[1,2,3], [4,5,6], [0,0,1]])
#print(matriz_a)

#atribui a matriz_b 3x3
matriz_b = np.array([[7,8,9],[10,11,12], [1,0,0]])
#print(matriz_b)

#realiza a soma das matrizes
soma = matriz_a + matriz_b
#print(soma)

#realiza o produto entre matrizes e apresenta
print(matriz_a @ matriz_b, "\n")

#Dá o determinante de uma matriz e apresenta
print(np.linalg.det(matriz_a), "\n")

#Dá a inversa de uma matriz e apresenta
print(np.linalg.inv(matriz_b), "\n")

#dá a transposta de uma matriz e apresenta
print(np.transpose(matriz_a), "\n")

print(np.floor((matriz_a @ np.linalg.inv(matriz_a))))

