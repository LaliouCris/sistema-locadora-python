class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        print(f"Cliente: {self.nome}")