# Caso de Estudio 3 Multicolinealidad en un modelo financiero-empresarial

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("datos.csv")

y = df["ROA"]
X = df[["activos", "ventas", "capital_trabajo"]]
X = sm.add_constant(X)

modelo_ols = sm.OLS(y, X).fit()
print(modelo_ols.summary())

corr = df[["activos", "ventas", "capital_trabajo"]].corr()
print(corr)

vif = pd.DataFrame()
vif["variable"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif)

X_reducido = sm.add_constant(df[["ventas", "capital_trabajo"]])
modelo_reducido = sm.OLS(y, X_reducido).fit()
print(modelo_reducido.summary())

scaler = StandardScaler()
X_std = scaler.fit_transform(df[["activos", "ventas", "capital_trabajo"]])

pca = PCA(n_components=1)
pc1 = pca.fit_transform(X_std)

X_pca = sm.add_constant(pc1)
modelo_pca = sm.OLS(y, X_pca).fit()
print(modelo_pca.summary())

#RESPUESTAS
"""
Sí existe multicolinealidad severa en el modelo, ya que los indicadores 
financieros presentan altas correlaciones entre sí y los factores de inflación
de varianza (VIF) son elevados, lo que se refleja en coeficientes con signos 
inesperados y falta de significancia estadística a pesar de un buen ajuste global
del modelo; esta multicolinealidad no sesga los estimadores, pero incrementa 
fuertemente sus varianzas y dificulta la interpretación individual de los coeficientes,
por lo que se recomienda eliminar variables redundantes, trabajar con ratios financieros 
o utilizar técnicas como análisis de componentes principales para obtener estimaciones más 
estables y económicamente interpretables.
"""