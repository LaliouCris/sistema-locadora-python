class Funcionario:
    def __init__(self, nome, cpf, idade, endereco, dados_contratacao, salario, quantidade_alugueis, status, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.dados_contratacao = dados_contratacao
        self.salario = salario
        self.quantidade_alugueis = quantidade_alugueis
        self.status = status
        self.telefone = telefone

    def exibir(self):
        print("===== FUNCIONÁRIO =====")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco}")
        print(f"Contratação: {self.dados_contratacao}")
        print(f"Salário: {self.salario}")
        print(f"Aluguéis realizados: {self.quantidade_alugueis}")
        print(f"Status: {self.status}")
        print(f"Telefone: {self.telefone}")