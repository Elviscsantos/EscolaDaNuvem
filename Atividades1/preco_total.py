# Calculadora de Preço Total
# Produto: "Cadeira Infantil", Preço unitário: R$ 12.40, Quantidade: 3
# Exibe todas as informações e o total formatado

def main():
    nome_produto = "Cadeira Infantil"
    preco_unitario = 12.40
    quantidade = 3
    preco_total = preco_unitario * quantidade

    print(f"Produto: {nome_produto}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R$ {preco_total:.2f}")

if __name__ == "__main__":
    main()
