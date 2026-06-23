from cliente import Cliente
from carro import Carro
from reserva import Reserva


print("================================")
print(" SISTEMA DE LOCAÇÃO DE VEÍCULOS ")
print("================================")

print("\n1 - Cadastrar cliente")
print("2 - Cadastrar carro")
print("3 - Fazer reserva")
print("4 - Sair")

opcao = input("\nEscolha uma opção: ")

if opcao == "1":
    nome = input("Nome do cliente: ")

    cliente = Cliente(nome)

    print("Cliente cadastrado com sucesso!")
    cliente.exibir()

elif opcao == "2":
    modelo = input("Modelo do carro: ")

    carro = Carro(modelo)

    print("Carro cadastrado com sucesso!")
    carro.exibir()

elif opcao == "3":
    nome_cliente = input("Nome do cliente: ")
    modelo_carro = input("Modelo do carro: ")

    reserva = Reserva(nome_cliente, modelo_carro)

    print("Reserva criada com sucesso!")
    reserva.exibir()

elif opcao == "4":
    print("Encerrando sistema...")

else:
    print("Opção inválida!")