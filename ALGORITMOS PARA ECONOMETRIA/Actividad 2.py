import numpy as np 
#Actividad 2: Tasa de Interés e Inversión Privada Banxico
Trimestre = [1,2,3,4,5]
Tasa_Interes_porcentual_X = [4.5,5.0,5.5,6.0,6.5]
Inversion_Privada_Y = [102,98,94,90,87]

X = np.array(Tasa_Interes_porcentual_X)
Y = np.array(Inversion_Privada_Y)

X_mean = np.mean(X)
Y_mean = np.mean(Y)

b = np.sum((X-X_mean)*(Y-Y_mean)) / np.sum((X-X_mean)**2)
a = Y_mean - b*X_mean
print(f"Ecuación de la recta: Y = {a:.2f} + {b:.2f}X")

#El signo de la pendiente es negativo, lo cual indica que a mayor tasa de Interés, menor inversión privada.
#Ahora, un Beta igual a 0 representa que no hay relacion alguna entre las variables 


#Predicción de la inversión privada cuando la tasa de interés es 5.8%
Y_pred = a + b*5.8
print(f"La inversión privada esperada cuando la tasa de interés es 5.8% es {Y_pred:.2f}")