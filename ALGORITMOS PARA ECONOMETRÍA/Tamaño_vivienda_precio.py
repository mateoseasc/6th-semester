import matplotlib.pyplot as plt
import numpy as np

# Precio de Vivienda segun su tamaño

tamaño_m2 = [50,60,70,80,90,150,180,220,260,300]
precio = [800,950,1100,1300,1550,2800,3500,4800,6200,8000]


#prueba de breusch pagan
from statsmodels.stats.diagnostic import het_breuschpagan
import statsmodels.api as sm

X = sm.add_constant(tamaño_m2)
model = sm.OLS(precio, X).fit()
bp_test = het_breuschpagan(model.resid, model.model.exog)
print(bp_test)

if bp_test[1] < 0.05:
    print("Hay heterocedasticidad")
else: 
    print("Hay homeocedasticidad")
