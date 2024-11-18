def adicionar_cliente(clientes):
    
    # Adiciona um novo cliente ao dicionário.
    
    id_cliente = input("Digite o ID do cliente: ").strip()
    if id_cliente in clientes:
        print("Erro: Já existe um cliente com esse ID.")
        return

    nome = input("Digite o nome do cliente: ").strip()
    email = input("Digite o e-mail do cliente: ").strip()
    clientes[id_cliente] = {"nome": nome, "email": email}
    print("Cliente adicionado com sucesso!")

def visualizar_clientes(clientes):
    
    # Exibe todos os clientes cadastrados.
    
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("Clientes cadastrados:")
        for id_cliente, info in clientes.items():
            print(f"ID: {id_cliente}, Nome: {info['nome']}, E-mail: {info['email']}")

def remover_cliente(clientes):
    
    # Remove um cliente do dicionário pelo ID.
    
    id_cliente = input("Digite o ID do cliente que deseja remover: ").strip()
    if id_cliente in clientes:
        del clientes[id_cliente]
        print("Cliente removido com sucesso!")
    else:
        print("Erro: Cliente não encontrado.")

def menu():
    
    # Menu principal do sistema de cadastro de clientes.
    
    clientes = {}
    while True:
        print("\n--- Sistema de Cadastro de Clientes ---")
        print("1. Adicionar cliente")
        print("2. Visualizar clientes")
        print("3. Remover cliente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_cliente(clientes)
        elif opcao == "2":
            visualizar_clientes(clientes)
        elif opcao == "3":
            remover_cliente(clientes)
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema
if __name__ == "__main__":
    menu()
