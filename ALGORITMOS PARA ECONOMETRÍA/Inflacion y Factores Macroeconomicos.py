# Inflación y Factores Macroeconómicos

Inflacion = [3.2,3.8,4.5,5.1,4.0,3.6]
Tipo_de_cambio = [18.5,19.0,19.8,20.5,20.0,19.5]
Tasa_de_interes = [6.0,6.5,7.0,7.5,7.0,6.5]
Crec_PIB = [2.5,2.0,3.0,1.5,2.8,3.2]

Y = Inflacion
X1 = Tipo_de_cambio
X2 = Tasa_de_interes
X3 = Crec_PIB

# Construye el Modelo
def Regresion_Lineal_Multiple(X1,X2,X3,Y):
    y_media = sum(Y)/len(Y)
    n = len(Y)
    X1_media = sum(X1)/len(X1)
    X2_media = sum(X2)/len(X2)
    X3_media = sum(X3)/len(X3)
    b1 = sum((X1[i]-X1_media)*(Y[i]-y_media) for i in range(n)) / sum((X1[i]-X1_media)**2 for i in range(n))
    b2 = sum((X2[i]-X2_media)*(Y[i]-y_media ) for i in range(n)) / sum((X2[i]-X2_media)**2 for i in range(n))
    b3 = sum((X3[i]-X3_media)*(Y[i]-y_media ) for i in range(n)) / sum((X3[i]-X3_media)**2 for i in range(n))
    b0 = y_media - b1*X1_media - b2*X2_media - b3*X3_media
    return b0,b1,b2,b3

b0,b1,b2,b3 = Regresion_Lineal_Multiple(X1,X2,X3,Y)
print(f"Modelo de Regresión Lineal Múltiple:\nInflación = {b0:.2f} + {b1:.2f}Tipo de Cambio + {b2:.2f}Tasa de Interés + {b3:.2f}Crecimiento del PIB")

"""
Inflación = -19.32 + 0.83Tipo de Cambio + 1.24Tasa de Interés + -0.50Crecimiento del PIB
el tipo de cambio aumenta la inflacion en .83 por cada unidad que aumenta el tipo de cambio, manteniendo constantes las otras variables.


¿Que variable controla la demanda agregada?
La tasa de interes, ya que al aumentar la tasa de interes, se desincentiva el consumo y la inversion, reduciendo la demanda agregada.

¿Que problemas econométricos pueden surgir?
Creo que la multicolinealidad puede ser un problema, ya que algunas variables macroeconomicas pueden estar correlacionadas entre si, lo que dificulta la estimacion precisa de los coeficientes del modelo.
"""