# importa a biblioteca numpy para ser usada no código, essa biblioteca manipula matrizes
import numpy as np
# importa a função de quadrados mínimos do arquivo Funcao_Quadrados_Minimos.py
from Funcao_Quadrados_Minimos import funcao_quadrados_minimos

# importa a função de geração de gráfico do arquivo Gerando_grafico.py
from Gerando_grafico import gerar_grafico

# criação da lista de pontos (x, y) a serem ajustados
x = [0, 2, 4, 5, 7, 10]
y = [10, 9, 7, 6, 3, 0]

# leitura do grau do polinômio a ser ajustado
n = int(input("Digite o grau do polinômio a ser ajustado: "))

# chama a função de quadrados mínimos para calcular os coeficientes do polinômio ajustado
coeficientes = funcao_quadrados_minimos(x, y, n)

# imprime os coeficientes do polinômio ajustado
print("Coeficientes do polinômio ajustado:", coeficientes)

# chama a função para gerar o gráfico do polinômio ajustado e dos pontos originais
gerar_grafico(x, y, coeficientes, n)

print("Fim")
