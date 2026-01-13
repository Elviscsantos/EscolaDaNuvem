# Calculadora de Média Escolar
# Dados:
# Nota 1: 7.5
# Nota 2: 8.0
# Nota 3: 6.5

def calcular_media(notas: list) -> float:
    return sum(notas) / len(notas)

def main():
    nota1 = 7.5
    nota2 = 8.0
    nota3 = 6.5
    notas = [nota1, nota2, nota3]

    media = calcular_media(notas)

    print("Calculadora de Média Escolar")
    print(f"Notas: {notas[0]:.2f}, {notas[1]:.2f}, {notas[2]:.2f}")
    print(f"Média: {media:.2f}")

if __name__ == '__main__':
    main()
