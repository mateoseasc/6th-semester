import pandas as pd

# 1. Datos del ejercicio (Output del VIF)
vif_data = pd.DataFrame({
    'Variable': ['X1', 'X2', 'X3'],
    'VIF': [12.4, 11.8, 1.3]
})

# 2. Umbral de decisión (Regla de dedo estándar)
UMBRAL_VIF = 10 

print("--- DIAGNÓSTICO AUTOMÁTICO ---")

# Detectar variables problemáticas
problemas = vif_data[vif_data['VIF'] > UMBRAL_VIF]

if not problemas.empty:
    print(f"⚠️  ALERTA: Se detectó Multicolinealidad Grave.")
    print(f"Variables afectadas: {problemas['Variable'].tolist()}")
    print("Justificación: Tienen un VIF superior a 10.")
else:
    print("✅ El modelo está limpio (No hay multicolinealidad severa).")

# Lógica para predicción
print("\n--- DECISIÓN DE USO ---")
print("¿Sirve para predecir? SÍ. La multicolinealidad no afecta la precisión de 'y_pred',")
print("solo afecta la interpretación individual de las betas.")