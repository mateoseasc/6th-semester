#CASO 3: Publicidad y Ventas

"Una empresa analiza si aumentar el gasto en publicidad"
"incrementa sus ventas mensuales"

Publicidad = [5,7,9,11,13]
Ventas = [20,24,28,32,36]

X = Publicidad
Y = Ventas

# Construye el Modelo
def Regresion_Lineal(X,Y):
    y_media = sum(Y)/len(Y)
    x_media = sum(X)/len(X)
    num = sum((X[i]-x_media)*(Y[i]-y_media) for i in range(len(X)))
    den = sum((X[i]-x_media)**2 for i in range(len(X)))
    b1 = num/den
    b0 = y_media - b1*x_media
    return b0,b1

b0,b1 = Regresion_Lineal(X,Y)
print(f"El modelo de regresión lineal es: Y = {b0:.2f} + {b1:.2f}X")

"""
¿Que representa B1 para la empresa?
- Representa el incremento en ventas por cada unidad invertida en Publicidad

¿Puede existir un punto donde la publicidad ya no funcione igual?
-Si

¿Que riesgos hay al usar una sola variable?
-Que la empresa invierta en publicidad sin considerar otros factores que pueden estar afectando sus ventas
asi que obtendrian un resultado no esperado perdiendo dinero 

"""

