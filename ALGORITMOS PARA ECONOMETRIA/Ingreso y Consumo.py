import matplotlib.pyplot as plt
import numpy as np

#EJERCICIO 1. INGRESO Y CONSUMO 

Ingreso = [5,6,7,8,9,15,18,22,25,30]
Consumo = [3.2,3.8,4.1,4.5,5.0,7.5,8.9,11.2,13.8,18.5]

#Regresion Lineal por el metodo de los minimos cuadrados
n = len(Consumo)
sum_x = sum(Ingreso)
media_x = sum_x / n
sum_y = sum(Consumo)
media_y = sum_y / n

pendiente = 0
numerador = 0
denominador = 0
for i in range(n):
    numerador += (Ingreso[i]-media_x) * (Consumo[i]-media_y)
    denominador+= (Ingreso[i]-media_x)**2
pendiente = numerador/denominador

intercepto = media_y - pendiente*media_x

y_hat = []
for x in Ingreso:
    y_hat.append(intercepto + pendiente * x)

residuos = []
for i in range(n):
    residuos.append(Consumo[i]-y_hat[i])


plt.scatter(Ingreso,Consumo, color = 'red')
plt.plot(Ingreso,y_hat)
plt.xlabel("Ingreso")
plt.ylabel("Consumo")
plt.title("Ingreso vs Consumo")
plt.show()

"""
¿La dispersión del error es constante?
    - No, no es constante ya que a medida que aumenta el ingreso, la varianza de los
    residuos también aumenta.


¿Existe heterocedasticidad? Explica.
Sí, existe heterocedasticidad ya que la varianza de los residuos no es constante


"""