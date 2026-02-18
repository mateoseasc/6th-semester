#CASO 1. Ingreso y Consumo de los Hogares (Economía básica)

X = [8,10,12,14,16]
Y = [4.5,5.2,6.0,6.8,7.5]

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
Y es es el consumo mensual de un hogar, la X es es el Ingreso mensual 
de un hogar, antes de llevar a cabo el modelo pensaria que Beta 1 es positivo ya que a mayor ingreso mayor consumo.
En el modelo no se incluyen otros factores, principalmente el error, que se atribuye a otras variables que influyen en el Consumo

"""