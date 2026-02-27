import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, het_white

df = pd.read_csv("mex_fin.csv")
columns = ["date","ipc","fix","rate"]
df = df[columns]

#MODELO DE REGRESION LINEAL MULTIPLE
Y = df["ipc"]
X = df[["fix","rate"]]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())

#PRUEBA DE BREUSCH-PAGAN
residuals = model.resid
bp_test = het_breuschpagan(residuals, X)
print(bp_test)

if bp_test[1] < 0.05:
    print("Rechazamos la hipótesis nula de homocedasticidad. Hay evidencia de heterocedasticidad.")
else:
    print("No rechazamos la hipótesis nula de homocedasticidad. No hay evidencia de heterocedasticidad.")


# GRAFICA DE RESIDUOS
plt.figure(figsize=(8,5))
plt.scatter(model.fittedvalues, residuals, color='blue', alpha=0.6)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Valores ajustados (predicciones)")
plt.ylabel("Residuos")
plt.title("Residuos vs Valores ajustados")
plt.show()
    