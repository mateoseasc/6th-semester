import numpy as np
# Actividad 1: Ingreso y consumo en hogares (INEGI - ENIGH)

Hogar = [1,2,3,4,5]
Ingreso_X = [6,8,10,12,14]
Consumo_Y = [4.9,5.6,6.3,7.0,7.6]

#Modelo de Regresión Lineal Simple
X = np.array(Ingreso_X)
Y = np.array(Consumo_Y)

X_mean = np.mean(X)
Y_mean = np.mean(Y)

b = np.sum((X-X_mean)*(Y-Y_mean)) / np.sum((X-X_mean)**2)
a = Y_mean - b*X_mean
print(f"Ecuación de la recta: Y = {a:.2f} + {b:.2f}X")

#Graficamos:
import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.plot(X, a + b*X, color='red')
plt.xlabel('Ingreso (X)')
plt.ylabel('Consumo (Y)')
plt.title('Regresión Lineal Simple')
plt.show()
#Predicción del consumo cuando el ingreso es 10
X_pred = 10
Y_pred = a + b*X_pred
print(f"El consumo esperado cuando el ingreso es {X_pred} es {Y_pred:.2f}")

#Interpretacion de los coeficientes:

#Intercepto: consumo esperado si el ingreso fuera 0 → 2.88

#Pendiente: el consumo sube 0.34 por cada unidad de ingreso

#Residuo en X=10, 0.02, el modelo es muy preciso para ese punto