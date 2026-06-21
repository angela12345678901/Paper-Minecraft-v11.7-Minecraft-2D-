import random

# Definición de las cajas con sus dos monedas
# 1 = Oro, 0 = Plata
cajas = {
    "C1":,  # Oro / Oro
    "C2":,  # Plata / Plata
    "C3": [1, 0]   # Oro / Plata
}

intentos_validos = 0
exitos = 0
iteraciones = 1_000_000

for _ in range(iteraciones):
    # 1. Elegir una caja al azar
    caja_elegida = random.choice(["C1", "C2", "C3"])
    monedas = cajas[caja_elegida].copy()
    
    # 2. Sacar una primera moneda al azar
    primera_moneda = random.choice(monedas)
    monedas.remove(primera_moneda)
    otra_moneda = monedas[0]
    
    # 3. Filtrar: Solo nos interesan los casos donde la primera es Oro (1)
    if primera_moneda == 1:
        intentos_validos += 1
        # Si la otra también es Oro, es un éxito
        if otra_moneda == 1:
            exitos += 1

# Calcular la probabilidad empírica
probabilidad_simulada = exitos / intentos_validos

print(f"Casos donde la primera moneda fue de Oro: {intentos_validos:,}")
print(f"Casos donde la segunda también fue de Oro: {exitos:,}")
print(f"Probabilidad experimental: {probabilidad_simulada:.4f} (Aprox. {probabilidad_simulada*100:.2f}%)")
