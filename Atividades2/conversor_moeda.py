# Conversor de Moeda
# Dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.20
# Taxa do euro: R$ 6.15

def converter_reais(valor_reais: float, taxa: float) -> float:
    return valor_reais / taxa

def main():
    valor_reais = 100.00
    taxa_dolar = 5.20
    taxa_euro = 6.15

    valor_dolar = converter_reais(valor_reais, taxa_dolar)
    valor_euro = converter_reais(valor_reais, taxa_euro)

    print("Conversor de Moeda")
    print(f"Valor em reais: R$ {valor_reais:.2f}")
    print(f"Taxa do dólar: R$ {taxa_dolar:.2f}  =>  Valor em dólares: $ {valor_dolar:.2f}")
    print(f"Taxa do euro:  R$ {taxa_euro:.2f}  =>  Valor em euros:  € {valor_euro:.2f}")

if __name__ == '__main__':
    main()
