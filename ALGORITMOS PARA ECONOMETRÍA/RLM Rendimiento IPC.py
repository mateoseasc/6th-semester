#Regresion Lineal Multivariable. Finanzas-Rendimiento del IPC y factores financieros
import numpy as np

r_ipc = [0.010, 0.015, 0.015, 0.0, 0.008, 0.012]
tasa = [7.25, 7.5, 7.75, 7.0, 7.25, 7.40]
volatilidad = [0.020, 0.030, 0.045, 0.018, 0.022, 0.028]

def regresion_lineal_multiple(Y, X1, X2):
    n = len(Y)
    X = np.column_stack((np.ones(n), X1, X2))
    Y = np.array(Y)
    beta = np.linalg.inv(X.T @ X) @ X.T @ Y
    return beta

beta = regresion_lineal_multiple(r_ipc, tasa, volatilidad)
beta
