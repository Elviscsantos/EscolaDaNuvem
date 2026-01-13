# Programa de Saudação com input
# Se o usuário apertar Enter sem digitar nada, usa "mundo" por padrão

def saudacao():
    nome = input("Digite seu nome (pressione Enter para 'mundo'): ").strip()
    if not nome:
        nome = "mundo"
    print(f"Olá, {nome}!")

if __name__ == "__main__":
    saudacao()
