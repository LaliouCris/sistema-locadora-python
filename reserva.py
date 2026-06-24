class Reserva:
    def __init__(self, codigo, cliente, carro, status, data_inicio, data_fim):
        self.codigo = codigo
        self.cliente = cliente
        self.carro = carro
        self.status = status
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def exibir(self):
        print("===== RESERVA =====")
        print(f"Código: {self.codigo}")
        print(f"Cliente: {self.cliente}")
        print(f"Carro: {self.carro}")
        print(f"Status: {self.status}")
        print(f"Data início: {self.data_inicio}")
        print(f"Data fim: {self.data_fim}")