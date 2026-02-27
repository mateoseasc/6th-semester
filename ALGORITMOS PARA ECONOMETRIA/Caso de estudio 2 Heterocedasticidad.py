#Caso de estudio 2 Heterocedasticidad en datos microeconómicos (corte transversal)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, het_white

df = pd.read_csv("datos.csv")

y = df["salario"]
X = df[["educacion", "experiencia"]]
X = sm.add_constant(X)

modelo_ols = sm.OLS(y, X).fit()
print(modelo_ols.summary())

residuos = modelo_ols.resid
ajustados = modelo_ols.fittedvalues

plt.figure()
plt.scatter(ajustados, residuos)
plt.axhline(0)
plt.show()

plt.figure()
plt.scatter(df["educacion"], residuos)
plt.axhline(0)
plt.show()

bp_test = het_breuschpagan(residuos, X)
print("Breusch-Pagan:", bp_test)

white_test = het_white(residuos, X)
print("White:", white_test)

modelo_robusto = modelo_ols.get_robustcov_results(cov_type="HC0")
print(modelo_robusto.summary())

df["log_salario"] = np.log(df["salario"])
y_log = df["log_salario"]

modelo_log = sm.OLS(y_log, X).fit()
print(modelo_log.summary())


#RESPUESTAS

"""
No se cumple el supuesto de varianza constante del error,
 ya que los residuos del modelo estimado por MCO muestran 
 un patrón sistemático al graficarse contra los valores 
 ajustados y contra la educación, y tanto la prueba de Breusch–Pagan 
 como la prueba de White rechazan la hipótesis nula de homocedasticidad; esto indica la presencia 
 de heterocedasticidad, por lo que el modelo original produce inferencia inválida, situación que se 
 corrige al reestimar el modelo utilizando errores estándar robustos de White o mediante una transformación
   logarítmica del salario, obteniéndose estimaciones más eficientes y pruebas de significancia confiables.



"""