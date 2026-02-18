#VIF y multicolinealidad (núcleo del tema)-Multicolinealidad

import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. Cargar los datos de la imagen
data = {
    'Tamano': [80, 100, 120, 150, 180, 200],
    'Habitaciones': [2, 3, 3, 4, 4, 5],
    'Banos': [1, 2, 2, 3, 3, 4]
}

df = pd.DataFrame(data)

# 2. Preparar variables para VIF
# Statsmodels requiere que agreguemos explícitamente una constante (intercepto)
X = df[['Tamano', 'Habitaciones', 'Banos']]
X_con_constante = sm.add_constant(X)

# 3. Calcular VIF para cada variable
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns # No incluimos la constante en el reporte final
# Calculamos VIF ignorando la primera columna (la constante) en el índice
vif_data["VIF"] = [variance_inflation_factor(X_con_constante.values, i) 
                   for i in range(1, len(X_con_constante.columns))]

print("--- Resultado del VIF ---")
print(vif_data)

# 4. Análisis de Multicolinealidad (Lógica para responder la preg 4)
print("\n--- Análisis ---")
limite_vif = 10 # Umbral común (a veces se usa 5)
for index, row in vif_data.iterrows():
    if row['VIF'] > limite_vif:
        print(f"La variable '{row['Variable']}' tiene multicolinealidad severa (VIF: {row['VIF']:.2f})")
    else:
        print(f"La variable '{row['Variable']}' está ok.")

"""
¿Qué variable presenta mayor VIF?
Habitaciones y Baños

¿Existe multicolinealidad? Justifica.
Justificación: Si el VIF es > 10 (algunos autores dicen > 5),
 indica que esa variable es redundante; es decir, se puede explicar 
 casi perfectamente usando una combinación lineal de las otras 
 variables del modelo.  
"""