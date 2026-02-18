#Ventas de una empresa y estrategia comercial (Administración)

Ventas = [120,135,140,150,145,160]
Publicidad = [10,12,14,15,13,16]
Precio = [20,19,18,18,19,17]
Promociones = [1,1,2,2,1,3]

Y = Ventas
X1 = Publicidad
X2 = Precio
X3 = Promociones

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
    a = y_media - b1*X1_media - b2*X2_media - b3*X3_media
    return a,b1,b2,b3


a,b1,b2,b3 = Regresion_Lineal_Multiple(X1,X2,X3,Y)
print(f"Ecuación de regresión lineal múltiple: Y = {a:.2f} + {b1:.2f}X1 + {b2:.2f}X2 + {b3:.2f}X3")

"""
Ecuación de regresión lineal múltiple: Y = 257.68 + 6.07X1 + -11.82X2 + 13.00X3

Interpreta el efecto del precio.
El precio afecta negativamente las ventas en -11.82 por cada unidad que aumenta el precio

¿Qué variable representa una decisión estratégica?
La publicidad, ya que la empresa decide cuanto gastar en ella para incrementar las ventas

¿Qué signo esperas para la publicidad?
Un signo positivo, ya que esta aumenta las ventas generalmente

¿Qué pasa si publicidad y promociones están correlacionadas?
Si aumentas la publicidad, es probable que aumenten las promociones, lo que 
dificulta aislar el efecto individual de cada variable en las ventas.

"""