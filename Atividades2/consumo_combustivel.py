# Calculadora de Consumo de Combustível
# Dados:
# Distância percorrida: 300 km
# Combustível gasto: 25 litros

def consumo_medio(distancia_km: float, litros_gastos: float) -> float:
    if litros_gastos == 0:
        return float('inf')
    return distancia_km / litros_gastos

def main():
    distancia = 300.0  # km
    litros = 25.0      # litros

    consumo = consumo_medio(distancia, litros)

    print("Calculadora de Consumo de Combustível")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Combustível gasto: {litros:.2f} litros")
    print(f"Consumo médio: {consumo:.2f} km/l")

if __name__ == '__main__':
    main()
