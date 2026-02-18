# =====================================================
# CASO DE ESTUDIO 1: AUTOCORRELACIÓN
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima.model import ARIMA

# =====================================================
# CARGA DE DATOS
# =====================================================

df = pd.read_csv("datos.csv")
df = df.sort_values("time")

y = df["y"]      # Consumo
x = df["x"]      # Ingreso

# =====================================================
# 1. MODELO MCO
# =====================================================

X = sm.add_constant(x)
modelo_ols = sm.OLS(y, X).fit()
print(modelo_ols.summary())

residuos = modelo_ols.resid

# =====================================================
# 2. RESIDUOS VS TIEMPO
# =====================================================

plt.figure()
plt.plot(df["time"], residuos)
plt.axhline(0)
plt.title("Residuos vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Residuos")
plt.show()

# =====================================================
# 3. ACF DE LOS RESIDUOS
# =====================================================

plot_acf(residuos, lags=20)
plt.title("ACF de los residuos")
plt.show()

# =====================================================
# 4. DURBIN-WATSON
# =====================================================

dw = durbin_watson(residuos)
print("Durbin-Watson:", dw)

# =====================================================
# 5. LJUNG-BOX
# =====================================================

ljung_box = acorr_ljungbox(residuos, lags=[10, 15, 20], return_df=True)
print(ljung_box)

# =====================================================
# 6. MODELO CON AR(1)
# =====================================================

modelo_ar1 = ARIMA(y, exog=x, order=(1,0,0)).fit()
print(modelo_ar1.summary())

residuos_ar1 = modelo_ar1.resid

plot_acf(residuos_ar1, lags=20)
plt.title("ACF residuos modelo AR(1)")
plt.show()

print("Ljung-Box AR(1)")
print(acorr_ljungbox(residuos_ar1, lags=[10], return_df=True))

# =====================================================
# 7. MODELO DINÁMICO
# =====================================================

df["y_lag"] = df["y"].shift(1)
df_dyn = df.dropna()

Y_dyn = df_dyn["y"]
X_dyn = sm.add_constant(df_dyn[["x", "y_lag"]])

modelo_dyn = sm.OLS(Y_dyn, X_dyn).fit()
print(modelo_dyn.summary())

residuos_dyn = modelo_dyn.resid

plot_acf(residuos_dyn, lags=20)
plt.title("ACF residuos modelo dinámico")
plt.show()

print("Ljung-Box modelo dinámico")
print(acorr_ljungbox(residuos_dyn, lags=[10], return_df=True))

#RESPUESTAS:

"""
Sí existe autocorrelación en los errores del modelo estimado por MCO,
ya que el estadístico Durbin-Watson es menor a 2 y la prueba de Ljung-Box
rechaza la hipótesis nula de no autocorrelación, lo cual es consistente 
además con los picos significativos observados en la función de autocorrelación
de los residuos; dicha autocorrelación es de corto plazo, puesto que la ACF muestra
significancia únicamente en los primeros rezagos y se disipa rápidamente conforme 
aumenta el rezago, lo que indica dependencia temporal limitada y no un proceso de memoria larga.
"""