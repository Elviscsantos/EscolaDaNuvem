# Script único com menu para executar os 4 exercícios
# Cada rotina aceita inputs com valores padrão (pressione Enter para usar o padrão)

import sys

def saudacao():
    nome = input("Digite seu nome (pressione Enter para 'mundo'): ").strip()
    if not nome:
        nome = "mundo"
    print(f"\nOlá, {nome}!\n")

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
    if isinstance(numero1, float) and numero1.is_integer() and isinstance(numero2, float) and numero2.is_integer():
        resultado = int(resultado)
    print(f"\nNúmero 1: {numero1}")
    print(f"Número 2: {numero2}")
    print(f"Soma: {resultado}\n")

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
    def fmt(x):
        return int(x) if isinstance(x, float) and x.is_integer() else round(x, 2) if isinstance(x, float) else x
    print(f"\nComprimento: {fmt(comprimento)} cm")
    print(f"Largura: {fmt(largura)} cm")
    print(f"Altura: {fmt(altura)} cm")
    print(f"Volume: {fmt(volume)} cm³\n")

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
    print(f"\nProduto: {nome_produto}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R$ {total:.2f}\n")

def mostrar_menu():
    print("Escolha uma opção:")
    print("1 - Saudação")
    print("2 - Calculadora de Soma")
    print("3 - Calculadora de Volume (caixa retangular)")
    print("4 - Calculadora de Preço Total")
    print("0 - Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input("Opção: ").strip()
        if opcao == "1":
            saudacao()
        elif opcao == "2":
            soma()
        elif opcao == "3":
            volume_caixa()
        elif opcao == "4":
            preco_total()
        elif opcao == "0":
            print("Saindo. Até logo!")
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
