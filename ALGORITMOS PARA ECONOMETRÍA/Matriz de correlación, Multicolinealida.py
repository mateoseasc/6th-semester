#Matriz de correlación, Multicolinealidad
import pandas as pd

data = {
    "Rend": [0.02, 0.01, -0.01, 0.03, 0.02],
    "Tasa": [7.0, 7.2, 7.4, 7.1, 7.3],
    "CETES": [6.9, 7.1, 7.3, 7.0, 7.2],
    "Inflacion": [4.1, 4.3, 4.5, 4.2, 4.4]
}

df = pd.DataFrame(data)

print(df.corr())

"""
Identifica pares con correlación alta.
Tasa y Cetes, Inflacion y Tasa, Inflacion y Cetes

¿Qué variables podrían causar multicolinealidad?
esas mismas

¿Cuál eliminarías y por qué?
Cetes, es una tasa y responde a la inflacion




"""