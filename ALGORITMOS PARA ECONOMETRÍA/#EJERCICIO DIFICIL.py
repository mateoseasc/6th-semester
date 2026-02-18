import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# =========================================================
# DATOS
# =========================================================
# Ingreso diario del restaurante (en dólares)
ingreso = np.array([
    1452, 1361, 1426, 1470, 1456,
    1430, 1354, 1442, 1394, 1459,
    1399, 1458, 1537, 1425, 1445,
    1439, 1348, 1450, 1431, 1446,
    1485, 1405, 1461, 1490, 1426
])

# Número de habitaciones ocupadas
habitaciones = np.array([
    23, 47, 21, 39, 37,
    29, 23, 44, 45, 16,
    30, 42, 54, 27, 34,
    15, 19, 38, 44, 47,
    43, 38, 51, 61, 39
])

# =========================================================
# a) DIAGRAMA DE DISPERSIÓN
# =========================================================
plt.figure()
plt.scatter(habitaciones, ingreso)
plt.xlabel("Habitaciones ocupadas")
plt.ylabel("Ingreso del restaurante")
plt.title("Ingreso del restaurante vs Habitaciones ocupadas")
plt.show()

print("a) Diagrama de dispersión")
print("Al observar el diagrama de dispersión, se aprecia una tendencia general")
print("positiva. A medida que aumenta el número de habitaciones ocupadas,")
print("el ingreso del restaurante tiende a aumentar, aunque existe dispersión.\n")

# =========================================================
# b) COEFICIENTE DE CORRELACIÓN
# =========================================================
r, p_value = stats.pearsonr(habitaciones, ingreso)

print("b) Coeficiente de correlación de Pearson")
print(f"r = {r:.3f}")
print("El coeficiente de correlación es positivo y de magnitud moderada,")
print("lo que indica una relación positiva moderada entre el número de")
print("habitaciones ocupadas y el ingreso del restaurante.\n")

# =========================================================
# c) PRUEBA DE HIPÓTESIS (α = 0.10)
# =========================================================
alpha = 0.10

print("c) Prueba de significancia (α = 0.10)")
print(f"p-value = {p_value:.3f}")

if p_value < alpha:
    print("Dado que el p-value es menor que el nivel de significancia,")
    print("se rechaza la hipótesis nula.")
    print("Es razonable concluir que existe una relación positiva")
    print("estadísticamente significativa entre ingreso y habitaciones ocupadas.\n")
else:
    print("No se rechaza la hipótesis nula.")
    print("No hay evidencia suficiente de una relación positiva.\n")

# =========================================================
# d) COEFICIENTE DE DETERMINACIÓN
# =========================================================
r_squared = r ** 2

print("d) Porcentaje de variación explicada")
print(f"R² = {r_squared:.3f}")
print(f"El {r_squared*100:.1f}% de la variación del ingreso del restaurante")
print("puede explicarse por el número de habitaciones ocupadas.")
print("El porcentaje restante se debe a otros factores.")
