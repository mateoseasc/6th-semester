#DEMANDA DE ENERGÍA ELÉCTRICA

Consumo = [100,102,105,98,108,110]
PIB = [2.5,2.0,3.0,1.5,3.2,3.5]
Temperatura = [22,23,24,21,25,26]
Precio_energia = [1.8,1.9,1.7,2.0,1.6,1.5]

Y = Consumo
X1 = PIB
X2 = Temperatura
X3 = Precio_energia

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
Ecuación de regresión lineal múltiple: Y = 72.15 + 5.64X1 + 2.49X2 + -23.71X3
¿Que variable representa el ingreso?
El PIB representa el ingreso, ya que un aumento en el PIB generalmente indica un aumento en el ingreso de los consumidores, lo que puede llevar a un mayor consumo de energía.

¿Qué signo esperas para el precio?
Espero un signo negativo para el precio de la energía, ya que un aumento en el precio generalmente conduce a una disminución en la demanda de energía.

¿Qué problema podría surgir al usar datos anuales?
El problema que podría surgir al usar datos anuales es que no capturan las variaciones estacionales y de corto plazo en la demanda de energía, lo que puede llevar a estimaciones inexactas del modelo.

"""
