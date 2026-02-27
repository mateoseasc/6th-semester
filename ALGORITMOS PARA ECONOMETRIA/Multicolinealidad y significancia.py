# Multicolinealidad y significancia

import pandas as pd
import statsmodels.api as sm

# 1. Crear el DataFrame con los datos de la imagen
data = {
    'Crecimiento': [2.1, 2.3, 2.5, 2.4, 2.6],
    'Inversion':   [18, 19, 20, 21, 22],
    'Ahorro':      [17, 18, 19, 20, 21]
}

df = pd.DataFrame(data)

# 2. Definir variables dependiente (y) e independientes (X)
X = df[['Inversion', 'Ahorro']]
y = df['Crecimiento']

# Añadir la constante (intercepto)
X = sm.add_constant(X)

# 3. Revisar correlación antes del modelo (Para confirmar la trampa)
print("--- Matriz de Correlación ---")
print(X.corr()) 
# Notarás que entre Inversion y Ahorro es 1.0 (Perfecta)

# 4. Estimar el modelo MCO
try:
    modelo = sm.OLS(y, X).fit()
    print("\n--- Resumen del Modelo ---")
    print(modelo.summary())
except Exception as e:
    print("\nError al estimar:", e)
    print("La multicolinealidad perfecta impide la inversión de la matriz.")


"""

¿Es posible que ninguna beta sea significativa?

SÍ. Es muy posible y es el síntoma principal.
Aunque el modelo global tenga un $R^2$ alto (el modelo predice bien),
 individualmente las variables salen como "no significativas" porque el
   modelo no sabe a cuál de las dos atribuirle el mérito del crecimiento.


¿Cómo lo relacionas con la multicolinealidad?
Al estar las variables correlacionadas (Inversión y Ahorro se mueven igual), 
es imposible distinguir el efecto individual de una manteniendo la otra constante 
(ceteris paribus), porque nunca cambian por separado.

Esto provoca que perdamos precisión, los intervalos de confianza se vuelvan gigantes 
y los contrastes de significancia (p-values) fallen, diciendo que las variables "no importan"
 cuando en realidad sí podrían importar.


"""