#CASO 5: Precio de vivienda y tamaño (Economía urbana/Finanzas)

Tamano_m2 = [60,80,100,120,140]
Precio = [900,1150,1400,1650,1900]

X = Tamano_m2
Y = Precio

def Regresion_Lineal(X,Y):
    y_media = sum(Y)/len(Y)
    x_media = sum(X)/len(X)
    b1 = sum([(X[i]-x_media)*(Y[i]-y_media) for i in range(len(X))]) / sum([(X[i]-x_media)**2 for i in range(len(X))])
    b0 = y_media - b1*x_media
    return b0,b1

b0,b1 = Regresion_Lineal(X,Y)

print(f"El modelo de regresión lineal es: Y = {b0:.2f} + {b1:.2f}X")

"""
¿Que indica B1?
- Beta 1 indica el cambio esperado en el Precio de la vivienda
por cada unidad adicional de tamaño en metros cuadrados.

¿Es razonable que dos casas del mismo tamaño tengan distinto precio?
- Si, ya que hay variables no consideradas en este modelo, si solo tomamos en cuenta el tamaño cetis paribus
ambas casas deberian de tener el mismo precio

¿Que variables faltan?
- Ubicacion, estado de la vivienda, edad de la vivienda, amenidades, etc

"""
