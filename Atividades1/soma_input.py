# Calculadora de Soma com input
# Usa numero1 = 12 e numero2 = 14 como padrão se o usuário apertar Enter

def soma():
    def ler_numero(prompt, default):
        entrada = input(f"{prompt} (padrão {default}): ").strip()
        if entrada == "":
            return default
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida — usando o valor padrão.")
            return default

    numero1 = ler_numero("Digite o número 1", 12)
    numero2 = ler_numero("Digite o número 2", 14)
    resultado = numero1 + numero2
    # Se ambos forem inteiros, exibe como inteiro; caso contrário, float
    if isinstance(numero1, float) and numero1.is_integer() and isinstance(numero2, float) and numero2.is_integer():
        resultado = int(resultado)
    print(f"Número 1: {numero1}")
    print(f"Número 2: {numero2}")
    print(f"Soma: {resultado}")

if __name__ == "__main__":
    soma()
