#Deteccion visual basica 

import numpy as np
import pandas as pd

# Datos
data = {
    "Ingreso": [10, 12, 14, 16, 18, 20],
    "Gasto": [9, 11, 13, 15, 17, 19]
}

df = pd.DataFrame(data)

# Correlación
correlacion = df["Ingreso"].corr(df["Gasto"])
print(correlacion)

#¿Qué observas?

"""
Observo una correlación de 1.0 lo que significa 
que al aumentar una, aumenta la otra proporcionalmente

No, no aportan informacion distinta al modelo ya que
estas directamente correlacionadas

Hay riesgo de multicolinealidad, si, literal eso es multicolinealidad
"""