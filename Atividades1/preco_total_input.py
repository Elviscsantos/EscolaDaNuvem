# Calculadora de Preço Total com input
# Padrões: produto="Cadeira Infantil", preco_unitario=12.40, quantidade=3

def preco_total():
    nome_padrao = "Cadeira Infantil"
    def ler_texto(prompt, default):
        entrada = input(f"{prompt} (padrão '{default}'): ").strip()
        return entrada if entrada != "" else default

    def ler_float(prompt, default):
        entrada = input(f"{prompt} (padrão {default}): ").strip()
        if entrada == "":
            return default
        try:
            return float(entrada.replace(",", "."))
        except ValueError:
            print("Entrada inválida — usando o valor padrão.")
            return default

    def ler_int(prompt, default):
        entrada = input(f"{prompt} (padrão {default}): ").strip()
        if entrada == "":
            return default
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida — usando o valor padrão.")
            return default

    nome_produto = ler_texto("Nome do produto", nome_padrao)
    preco_unitario = ler_float("Preço unitário (use . ou , como separador decimal)", 12.40)
    quantidade = ler_int("Quantidade", 3)
    total = preco_unitario * quantidade

    print(f"Produto: {nome_produto}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R$ {total:.2f}")

if __name__ == "__main__":
    preco_total()
