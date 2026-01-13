# Calculadora de Desconto
# Dados:
# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20%

def calcular_desconto(preco: float, porcentagem: float) -> tuple:
    desconto = preco * (porcentagem / 100)
    preco_final = preco - desconto
    return desconto, preco_final

def main():
    nome_produto = "Camiseta"
    preco_original = 50.00
    percentual_desconto = 20.0

    desconto, preco_final = calcular_desconto(preco_original, percentual_desconto)

    print("Calculadora de Desconto")
    print(f"Produto: {nome_produto}")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Porcentagem de desconto: {percentual_desconto:.0f}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")

if __name__ == '__main__':
    main()
