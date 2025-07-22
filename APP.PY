# app.py

def main():
    """
    Função principal do aplicativo.
    Pede o nome do usuário e exibe uma saudação.
    """
    print("Olá! Bem-vindo ao meu primeiro aplicativo Python.")
    nome = input("Por favor, digite seu nome: ")

    if nome:
        print(f"Olá, {nome}! É um prazer conhecê-lo.")
    else:
        print("Parece que você não digitou um nome. Tudo bem!")

    print("Obrigado por usar o aplicativo!")

# Este bloco garante que a função main() seja chamada apenas quando o script for executado diretamente.
if __name__ == "__main__":
    main()
