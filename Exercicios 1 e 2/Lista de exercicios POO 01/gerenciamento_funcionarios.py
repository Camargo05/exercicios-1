class Funcionario:
    def __init__(self, nome, id_func, salario, departamento):
        self.nome = nome
        self.id = id_func
        self.salario = salario
        self.departamento = departamento

    def __str__(self):
        return f"Funcionario[ID={self.id}, Nome='{self.nome}', Salário=R${self.salario:.2f}, Depto='{self.departamento}']"

def gerenciador_funcionarios():
    funcionarios = []

    while True:
        print("\n--- Sistema de Gerenciamento de Funcionários ---")
        print("1. Cadastrar Funcionário")
        print("2. Calcular Salário Total por Departamento")
        print("3. Listar todos os Funcionários")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                nome = input("Nome: ")
                id_func = int(input("ID: "))
                salario = float(input("Salário: "))
                depto = input("Departamento: ")
                funcionarios.append(Funcionario(nome, id_func, salario, depto))
                print("Funcionário cadastrado com sucesso!")
            except ValueError:
                print("Erro: ID e Salário devem ser números.")
        
        elif opcao == '2':
            depto_busca = input("Digite o nome do departamento: ")
            total_salarios = sum(f.salario for f in funcionarios if f.departamento.lower() == depto_busca.lower())
            print(f"O total de salários para o departamento '{depto_busca}' é: R${total_salarios:.2f}")

        elif opcao == '3':
            print("\n--- Lista de Funcionários Cadastrados ---")
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for f in funcionarios:
                    print(f)

        elif opcao == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

gerenciador_funcionarios()