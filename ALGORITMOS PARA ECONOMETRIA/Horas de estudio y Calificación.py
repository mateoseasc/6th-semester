#Caso 2: Horas de estudio y calificaciones

hrs = [2,4,6,8,10]
calificacion = [60,68,75,82,88]

X = hrs
Y = calificacion

# Construye el Modelo
def Regresion_Lineal(X,Y):
    y_media = sum(Y)/len(Y)
    x_media = sum(X)/len(X)
    b1 = sum([(X[i]-x_media)*(Y[i]-y_media) for i in range(len(X))])/sum([(X[i]-x_media)**2 for i in range(len(X))])
    b0 = y_media - b1*x_media
    return b0,b1

b0,b1 = Regresion_Lineal(X,Y)
print(f"El modelo de regresión lineal es: Y = {b0:.2f} + {b1:.2f}X")

"""
¿Que significa el intercepto B0?
-El intercepto B0 representa el valor de Y(Calificacion)cuando X(Horas de estudio) es igual a 0.

¿Es realista pensar que solo estudiar explica la calificación obtenida?
- No, no es realista pensar eso, hay mas variables que influyen en sacar una buena calificacion

¿Que variables pueden influir?
- La calidad del estudio, el sueño, estado anímico, concentracion, etc.
"""