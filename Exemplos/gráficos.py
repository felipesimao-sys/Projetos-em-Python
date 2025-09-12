# importa a biblioteca numpy para ser usada no código, essa biblioteca manipula matrizes
import numpy as np
# importa a biblioteca matplotlib para ser usada no código, essa biblioteca cria os gráficos
import matplotlib.pyplot as plt

# entre com os valores para x e y
x = [0, 2, 4, 5, 8, 10]
y = [10, 9, 7, 6, 3, 0]

#Comando para criar p gráfico com base nos valores passados
plt.plot(x, y)
#Exibe o gráfico com as informações passadas
plt.show()
print("Fim")
