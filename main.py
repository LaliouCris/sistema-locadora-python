from cliente import Cliente
from carro import Carro, Esportivo, Importado
from reserva import Reserva
from funcionario import Funcionario
from promocao import Promocao


clientes = []
carros = []
reservas = []
funcionarios = []
promocoes = []


while True:
    print("\n================================")
    print(" SISTEMA DE LOCAÇÃO DE VEÍCULOS ")
    print("================================")

    print("\n1 - Cadastrar cliente")
    print("2 - Cadastrar carro")
    print("3 - Fazer reserva")
    print("4 - Cadastrar funcionário")
    print("5 - Cadastrar promoção")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        nascimento = input("Data de nascimento: ")
        numero_cnh = input("Número da carteira de motorista: ")
        foto_cnh = input("Foto da carteira de motorista: ")
        vencimento_cnh = input("Ano de vencimento da carteira: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")

        cliente = Cliente(nome, cpf, idade, nascimento, numero_cnh, foto_cnh, vencimento_cnh, endereco, telefone, email)
        clientes.append(cliente)

        print("\nCliente cadastrado com sucesso!")
        cliente.exibir()

    elif opcao == "2":
        print("\nTipo de carro:")
        print("1 - Comum")
        print("2 - Esportivo")
        print("3 - Importado")

        tipo = input("Escolha o tipo de carro: ")

        placa = input("Placa: ")
        ano = input("Ano: ")
        cor = input("Cor: ")
        modelo = input("Modelo: ")
        quilometragem = input("Quilometragem: ")
        valor_diaria = input("Valor diário: ")
        observacao = input("Observação: ")

        if tipo == "1":
            carro = Carro(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao)

        elif tipo == "2":
            tempo_100_milhas = input("Tempo para chegar a 100 milhas/h: ")
            melhorias = input("Lista de melhorias: ")
            carro = Esportivo(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao, tempo_100_milhas, melhorias)

        elif tipo == "3":
            quantidade_passageiros = input("Quantidade de passageiros: ")
            tamanho_bagageiro = input("Tamanho do bagageiro: ")
            km_por_litro = input("Km por litro de gasolina: ")
            carro = Importado(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao, quantidade_passageiros, tamanho_bagageiro, km_por_litro)

        else:
            carro = None
            print("\nTipo de carro inválido!")

        if carro is not None:
            carros.append(carro)
            print("\nCarro cadastrado com sucesso!")
            carro.exibir()

    elif opcao == "3":
        cpf_cliente = input("Digite o CPF do cliente: ")

        cliente_encontrado = None

        for cliente in clientes:
            if cliente.cpf == cpf_cliente:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            print("\nCliente não encontrado. Cadastre o cliente primeiro.")

        elif cliente_encontrado.reserva_ativa is not None:
            print("\nEste cliente já possui uma reserva ativa.")
            cliente_encontrado.reserva_ativa.exibir()

        else:
            placa_carro = input("Digite a placa do carro: ")

            carro_encontrado = None

            for carro in carros:
                if carro.placa == placa_carro:
                    carro_encontrado = carro
                    break

            if carro_encontrado is None:
                print("\nCarro não encontrado. Cadastre o carro primeiro.")

            else:
                codigo = input("Código da reserva: ")
                status = input("Status da reserva: ")
                data_inicio = input("Data início: ")
                data_fim = input("Data fim: ")

                reserva = Reserva(codigo, cliente_encontrado.nome, carro_encontrado.modelo, status, data_inicio, data_fim)

                cliente_encontrado.reserva_ativa = reserva
                reservas.append(reserva)

                print("\nReserva criada com sucesso!")
                reserva.exibir()

    elif opcao == "4":
        nome = input("Nome do funcionário: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        endereco = input("Endereço: ")
        dados_contratacao = input("Dados da contratação: ")
        salario = input("Salário: ")
        quantidade_alugueis = input("Quantidade de aluguéis realizados: ")
        status = input("Status do funcionário: ")
        telefone = input("Telefone: ")

        funcionario = Funcionario(nome, cpf, idade, endereco, dados_contratacao, salario, quantidade_alugueis, status, telefone)
        funcionarios.append(funcionario)

        print("\nFuncionário cadastrado com sucesso!")
        funcionario.exibir()

    elif opcao == "5":
        titulo = input("Título da promoção: ")
        descricao = input("Descrição da promoção: ")
        validade = input("Validade da promoção: ")

        promocao = Promocao(titulo, descricao, validade)
        promocoes.append(promocao)

        print("\nPromoção cadastrada com sucesso!")
        promocao.exibir()

    elif opcao == "6":
        print("\nEncerrando sistema...")
        break

    else:
        print("\nOpção inválida!")