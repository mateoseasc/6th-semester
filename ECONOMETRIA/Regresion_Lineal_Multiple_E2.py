#Ejercicio 2
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

Y = [50,52,55,53,56,58]
X1 = [80,82,85,83,88,90]
X2 = [4.0,4.5,4.0,5.0,4.2,4.0]
X3 = [6.0,6.5,6.0,7.0,6.2,6.0]

beta = regresion_lineal_multiple(X1, X2, X3, Y)

print("β0 (intercepto):", beta[0])
print("β1 Remesas:", beta[1])
print("β2 Inversión:", beta[2])
print("β3 Apertura:", beta[3])
