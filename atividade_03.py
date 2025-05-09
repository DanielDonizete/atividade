def main():
    banco = ""
    conta = ""
    nome = ""
    idade = 0

    while True:
        print("\nMenu")
        print("1.Cadastrar banco / Tipo de conta: ")
        print("2.Cadastrar usuario: ")
        print("3.Dados cadastrados: ")
        print("4.Sair do sistema! ")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            banco = input("banco: ")
            conta = input("Digite o tipo de conta desejada: ")
            print("Banco cadastrado!")

        elif opcao == "2":
            if banco:
                nome = input("nome: ")
                idade = input("idade: ")
                print ("Usuario cadastrado")
            else:
                print("Usuario nao cadastrado")

        elif opcao == "3":
            if nome:
                print(f"\nNome:{nome}")
                print(f"Idade:{idade}")
                print(f"\nBanco:{banco}")
                print(f"Conta:{conta}")
            else:
                print("Usuario nao cadastrado")


        elif opcao == "4":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


if __name__=="__main__":
     main()
        
           
