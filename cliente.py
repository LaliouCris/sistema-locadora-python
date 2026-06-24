class Cliente:
    def __init__(
        self,
        nome,
        cpf,
        idade,
        nascimento,
        numero_cnh,
        foto_cnh,
        vencimento_cnh,
        endereco,
        telefone,
        email
    ):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.nascimento = nascimento
        self.numero_cnh = numero_cnh
        self.foto_cnh = foto_cnh
        self.vencimento_cnh = vencimento_cnh
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print("===== CLIENTE =====")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        print(f"Nascimento: {self.nascimento}")
        print(f"CNH: {self.numero_cnh}")
        print(f"Foto CNH: {self.foto_cnh}")
        print(f"Vencimento_CNH: {self.vencimento_cnh}")
        print(f"Endereco: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")