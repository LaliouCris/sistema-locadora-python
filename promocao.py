class Promocao:
    def __init__(self, titulo, descricao, validade):
        self.titulo = titulo
        self.descricao = descricao
        self.validade = validade

    def exibir(self):
        print("===== PROMOÇÃO =====")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Validade: {self.validade}")