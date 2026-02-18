import matplotlib.pyplot as plt
import numpy as np

# PUBLICIDAD Y VENTAS
publicidad = np.array([2,3,4,5,6,10,12,15,18,20])
ventas = np.array([10,13,15,18,21,30,40,55,80,110])

n = len(publicidad)

# Medias
media_x = np.mean(publicidad)
media_y = np.mean(ventas)

# OLS
numerador = 0
denominador = 0

for i in range(n):
    numerador += (publicidad[i] - media_x) * (ventas[i] - media_y)
    denominador += (publicidad[i] - media_x) ** 2

pendiente = numerador / denominador
intercepto = media_y - pendiente * media_x

# Valores ajustados
y_hat = intercepto + pendiente * publicidad

# Residuos
residuos = ventas - y_hat

# Gráfica residuos vs valores ajustados
plt.scatter(y_hat, residuos)
plt.axhline(0, linestyle='--')
plt.xlabel("Valores ajustados de Ventas")
plt.ylabel("Residuos")
plt.title("Residuos vs Valores Ajustados")
plt.show()



"""
Describe el patrón de los residuos.
-Comienzan positivos, luego se vuelven negativos y finalmente vuelven a ser positivos


¿Por qué es razonable esperar heterocedasticidad en este caso?
Por que a medida que aumentan las ventas, habrá otros factores que influyen
en estas mismas, no solo la publicidad, entonces quizas ya corregiste
la falta de marketing pero hay otros factores que disparan el error.




"""