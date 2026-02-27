# Salud pública: gasto y esperanza de vida
"""
País	Esperanza vida (Y)	Gasto salud (X₁)	PIB per cápita (X₂)	Médicos/1000 (X₃)
A	72	5.0	9	1.8
B	75	6.5	11	2.1
C	78	7.0	14	2.5
D	80	8.0	18	3.0
E	82	9.0	22	3.5
F	83	9.5	25	3.8
"""

Y = [72, 75, 78, 80, 82, 83]
X1 = [5.0, 6.5, 7.0, 8.0, 9.0, 9.5]
X2 = [9, 11, 14, 18, 22, 25]
X3 = [1.8, 2.1, 2.5, 3.0, 3.5, 3.8]

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
Ecuación de regresión lineal múltiple: Y = 34.18 + 2.50X1 + 0.65X2 + 5.25X3
¿Qué variable controla el nivel de desarrollo?
EL PIB


Interpreta el coeficiente del gasto en salud.
Es el coeficiente b1 = 2.5, lo que indica que por cada unidad adicional de gasto en salud
se espera que la esperanza de vida aumente en 2.5 años, ceteris paribus.

¿Qué problema de endogeneidad puede existir?
Un posible problema es que el gasto en salud y el PIB esten correlacionados con otros
factores no observados en el modelo

¿Qué otra variable social incluirías?
El nivel educativo promedio de la poblacion





"""