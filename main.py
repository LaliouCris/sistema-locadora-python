from cliente import Cliente
from carro import Carro, Esportivo, Importado
from reserva import Reserva
from funcionario import Funcionario
from promocao import Promocao


print("================================")
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
    numero_cnh = input("Número da CNH: ")
    foto_cnh = input("Foto da CNH: ")
    vencimento_cnh = input("Vencimento da CNH: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    cliente = Cliente(nome, cpf, idade, nascimento, numero_cnh, foto_cnh, vencimento_cnh, endereco, telefone, email)

    print("Cliente cadastrado com sucesso!")
    cliente.exibir()

elif opcao == "2":
    print("\nTipo de carro:")
    print("1 - Comum")
    print("2 - Esportivo")
    print("3 - Importado")

    tipo = input("Escolha o tipo: ")

    placa = input("Placa: ")
    ano = input("Ano: ")
    cor = input("Cor: ")
    modelo = input("Modelo: ")
    quilometragem = input("Quilometragem: ")
    valor_diaria = input("Valor da diária: ")
    observacao = input("Observação: ")

    if tipo == "1":
        carro = Carro(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao)

    elif tipo == "2":
        tempo_100_milhas = input("Tempo até 100 milhas/h: ")
        melhorias = input("Lista de melhorias: ")
        carro = Esportivo(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao, tempo_100_milhas, melhorias)

    elif tipo == "3":
        quantidade_passageiros = input("Quantidade de passageiros: ")
        tamanho_bagageiro = input("Tamanho do bagageiro: ")
        km_por_litro = input("Km por litro: ")
        carro = Importado(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao, quantidade_passageiros, tamanho_bagageiro, km_por_litro)

    else:
        carro = None
        print("Tipo de carro inválido!")

    if carro is not None:
        print("Carro cadastrado com sucesso!")
        carro.exibir()

elif opcao == "3":
    codigo = input("Código da reserva: ")
    cliente = input("Nome do cliente: ")
    carro = input("Modelo do carro: ")
    data_inicio = input("Data início: ")
    data_fim = input("Data fim: ")
    status = input("Status: ")

    reserva = Reserva(codigo, cliente, carro, data_inicio, data_fim, status)

    print("Reserva criada com sucesso!")
    reserva.exibir()

elif opcao == "4":
    nome = input("Nome do funcionário: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    endereco = input("Endereço: ")
    dados_contratacao = input("Dados da contratação: ")
    salario = input("Salário: ")
    quantidade_alugueis = input("Quantidade de aluguéis realizados: ")
    status = input("Status: ")
    telefone = input("Telefone: ")

    funcionario = Funcionario(nome, cpf, idade, endereco, dados_contratacao, salario, quantidade_alugueis, status, telefone)

    print("Funcionário cadastrado com sucesso!")
    funcionario.exibir()

elif opcao == "5":
    titulo = input("Título da promoção: ")
    descricao = input("Descrição: ")
    validade = input("Validade: ")

    promocao = Promocao(titulo, descricao, validade)

    print("Promoção cadastrada com sucesso!")
    promocao.exibir()

elif opcao == "6":
    print("Encerrando sistema...")

else:
    print("Opção inválida!")