# Calculadora de Volume de uma caixa retangular com input
# Padrões: comprimento=12, largura=14, altura=20 (cm)

def volume_caixa():
    def ler_medida(prompt, default):
        entrada = input(f"{prompt} em cm (padrão {default}): ").strip()
        if entrada == "":
            return default
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida — usando o valor padrão.")
            return default

    comprimento = ler_medida("Comprimento", 12)
    largura = ler_medida("Largura", 14)
    altura = ler_medida("Altura", 20)
    volume = comprimento * largura * altura
    # Mostra valores com até 2 casas decimais quando necessário
    def fmt(x):
        return int(x) if isinstance(x, float) and x.is_integer() else round(x, 2) if isinstance(x, float) else x
    print(f"Comprimento: {fmt(comprimento)} cm")
    print(f"Largura: {fmt(largura)} cm")
    print(f"Altura: {fmt(altura)} cm")
    print(f"Volume: {fmt(volume)} cm³")

if __name__ == "__main__":
    volume_caixa()
