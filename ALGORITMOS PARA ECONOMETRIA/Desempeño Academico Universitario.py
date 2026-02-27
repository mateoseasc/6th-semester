#Desempeño académico universitario

Promedio = [78,82,75,88,90,85]
Horas_Estudio = [10,12,8,15,16,14]
Asistencia = [80,85,78,90,92,88]
Horas_trabajo = [20,15,25,10,8,12]

Y = Promedio
X1 = Horas_Estudio
X2 = Asistencia
X3 = Horas_trabajo

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
Ecuación de regresión lineal múltiple: Y = -15.60 + 1.87X1 + 1.04X2 + -0.89X3

La variable con efecto negativo son las Horas de Trabajo

¿Es razonable una relacion lineal?
Sí, es razonable asumir una relación lineal entre las variables 
independientes (Horas de Estudio, Asistencia y Horas de Trabajo) y 
la variable dependiente (Promedio). 

¿Que variable faltante podria mejorar el modelo?
Una variable que podría mejorar el modelo es el "Nivel de Estrés" del estudiante.
"""

