#Regresión Lineal Simple

import numpy as np

import numpy as np

def regresion_lineal_simple(x, y):
    x = np.asarray(x)
    y = np.asarray(y)

    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud")

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    cov = np.mean((x - x_mean) * (y - y_mean))
    var = np.mean((x - x_mean)**2)

    if var == 0:
        raise ValueError("La varianza de x es cero")

    m = cov / var
    b = y_mean - m * x_mean

    return m, b
