import numpy as np
#Actividad 3: Precio del petróleo e inflación (Banco Mundial)
Ano = [1,2,3,4,5]
Precio_Petroleo = [45,55,65,75,85]
Inflacion = [3.1,3.6,4.0,4.6,5.1]
#Graficamos los datos
import matplotlib.pyplot as plt
plt.scatter(Precio_Petroleo,Inflacion)
plt.plot(Precio_Petroleo,Inflacion, color='red')
plt.xlabel('Precio del petróleo')
plt.ylabel('Inflación')
plt.title('Relación entre Precio del Petróleo e Inflación')
plt.grid(True)
plt.show()




#Modelo de regresión lineal simple
X = np.array(Precio_Petroleo)
Y = np.array(Inflacion)

X_mean = np.mean(X)
Y_mean = np.mean(Y)

b = np.sum((X-X_mean)*(Y-Y_mean)) / np.sum((X-X_mean)**2)
a = Y_mean - b*X_mean
print(f"Ecuación de la recta: Y = {a:.2f} + {b:.2f}X")

#El intercepto a es el valor de Y cuando X es 0

#Residuo ultimo año
Y_pred = a + b*X
residuo_ultimo_ano = Y[-1] - Y_pred[-1]
print(f"El residuo del último año es {residuo_ultimo_ano:.2f}")

#El residuo del ultimo año es la diferencia entre el valor real de inflación y el valor predicho por el modelo para el último año.