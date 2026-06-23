class Reserva:
    def __init__(self, cliente, carro):
        self.cliente = cliente
        self.carro = carro

    def exibir(self):
        print("===== RESERVA =====")
        print(f"Cliente: {self.cliente}")
        print(f"Carro: {self.carro}")