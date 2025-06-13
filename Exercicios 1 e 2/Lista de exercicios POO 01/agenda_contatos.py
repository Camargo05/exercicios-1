class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    def __str__(self):
        return f"Contato[Nome='{self.nome}', Tel='{self.telefone}', Email='{self.email}']"

def agenda_contatos():
    agenda = []
    LIMITE_CONTATOS = 10

    while True:
        print("\n--- Agenda de Contatos ---")
        print(f"({len(agenda)}/{LIMITE_CONTATOS} contatos)")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Procurar Contato por Nome")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if len(agenda) >= LIMITE_CONTATOS:
                print("A agenda está cheia! Não é possível adicionar mais contatos.")
                continue
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.append(Contato(nome, telefone, email))
            print("Contato adicionado com sucesso!")
        
        elif opcao == '2':
            print("\n--- Lista de Contatos ---")
            if not agenda:
                print("Nenhum contato na agenda.")
            else:
                for contato in agenda:
                    print(contato)
        
        elif opcao == '3':
            nome_busca = input("Digite o nome do contato a ser procurado: ")
            encontrado = False
            for contato in agenda:
                if contato.nome.lower() == nome_busca.lower():
                    print("Contato encontrado:")
                    print(f"  Telefone: {contato.telefone}")
                    print(f"  Email: {contato.email}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"Contato com o nome '{nome_busca}' não foi encontrado.")

        elif opcao == '4':
            print("Encerrando a agenda...")
            break
        else:
            print("Opção inválida. Tente novamente.")

agenda_contatos()