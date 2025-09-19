# Esse programa o vetor gradiente a aprtir da formula f(x) = Mx-c, onde M é uma matriz, x é um vetor e c é um vetor
import numpy as np


def vetor_gradiente(M, x, c):
    M = np.array(M)
    x = np.array(x)
    c = np.array(c)
    g = M @ x - c
    return g
