# importa a biblioteca numpy para ser usada no código, essa biblioteca manipula matrizes
import numpy as np
# importa a biblioteca matplotlib para ser usada no código, essa biblioteca cria os gráficos
import matplotlib.pyplot as plt

#cria a função que gera o gráfico do polinômio ajustado e dos pontos originais
def gerar_grafico(x, y, coeficientes):
    # Gera valores de x para o gráfico do polinômio ajustado
    x_grafico = np.linspace(min(x), max(x), 100)
    
    # Calcula os valores de y do polinômio ajustado usando os coeficientes fornecidos
    y_grafico = sum(c * x_grafico**i for i, c in enumerate(coeficientes))
    
    # Cria o gráfico
    plt.plot(x_grafico, y_grafico, label='Polinômio Ajustado', color='blue')
    plt.scatter(x, y, color='red', label='Pontos Originais')
    
    # Adiciona título e rótulos aos eixos
    plt.title('Ajuste por Mínimos Quadrados')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Adiciona uma legenda
    plt.legend()
    
    # Exibe o gráfico
    plt.show()