#EJERCICIO 3
import numpy as np

def regresion_lineal_multiple(X1, X2, X3, Y):
    # Convertir a numpy arrays
    X1 = np.array(X1)
    X2 = np.array(X2)
    X3 = np.array(X3)
    Y = np.array(Y)

    n = len(Y)

    # Matriz X con intercepto
    X = np.column_stack((np.ones(n), X1, X2, X3))

    # Fórmula beta = (XᵀX)^(-1) XᵀY
    beta = np.linalg.inv(X.T @ X) @ X.T @ Y

    return beta

Y  = [2.1, 1.8, 2.5, 1.2, 2.8]
X1 = [3.0, 3.5, 4.0, 4.5, 5.0]
X2 = [20, 19, 21, 18, 22]
X3 = [60, 58, 62, 57, 63]

beta = regresion_lineal_multiple(X1, X2, X3, Y)

print("β0 (intercepto):", beta[0])
print("β1 Remesas:", beta[1])
print("β2 Inversión:", beta[2])
print("β3 Apertura:", beta[3])