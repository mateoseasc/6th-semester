import matplotlib.pyplot as plt
import numpy as np

# Rendimiento según nivel de riesgo

riesgo = [0.5, 0.6, 0.7, 0.8, 0.9, 1.5, 1.7, 2.0, 2.3, 2.8]
rendimiento = [0.01, 0.015, 0.018, 0.020, 0.025, -0.10, 0.15, -0.20, 0.30, -0.40]

# Prueba de Breusch-Pagan
from statsmodels.stats.diagnostic import het_breuschpagan
import statsmodels.api as sm

X = sm.add_constant(riesgo)
model = sm.OLS(rendimiento, X).fit()
bp_test = het_breuschpagan(model.resid, model.model.exog)

print(bp_test)

if bp_test[1] < 0.05:
    print("Hay heterocedasticidad")
else:
    print("Hay homocedasticidad")


import matplotlib.pyplot as plt

#Grafica de Residuos
residuos = model.resid
plt.scatter(model.fittedvalues, residuos)
plt.axhline(0, linestyle='--')
plt.xlabel("Valores ajustados de Rendimiento")
plt.ylabel("Residuos")
plt.title("Residuos vs Valores Ajustados")
plt.show()

"""


¿Qué sucede con la varianza del error cuando el riesgo aumenta?
 -aumenta

¿Este comportamiento es típico en finanzas?
 -si, a mayor riesgo, mayor rendimiento, pero tambien mayor incertidumbre


"""






