#CASO 4: Tipo de cambio e inflación (Macroeconomía)

Tipo_de_cambio = [18.5,19.0,19.8,20.5,21.0]
Inflacion = [3.2,3.8,4.5,5.1,5.6]

X = Tipo_de_cambio
Y = Inflacion

def Regresion_Lineal(X,Y):
    y_media = sum(Y)/len(Y)
    x_media = sum(X)/len(X)
    b1 = sum([(X[i]-x_media)*(Y[i]-y_media) for i in range(len(X))]) / sum([(X[i]-x_media)**2 for i in range(len(X))])
    b0 = y_media - b1 * x_media
    return b0,b1

b0,b1 = Regresion_Lineal(X,Y)
print(f"El modelo de regresión lineal es: Y = {b0:.2f} + {b1:.2f}X")


"""
¿Como interpretas una pendiente positiva?
-Que al aumentar la X, la Y también aumenta.

¿Que significa que el peso se deprecie?
-Significa que el peso se deprecie, significa que el tipo de cambio aumentó

¿Es correcto usar solo el tipo de cambio para explicar la inflación?
-No, hay muchos otros factores que influyen en el Incremento o Decremento de la inflación, no solo 
el tipo de cambio.

"""