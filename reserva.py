class Reserva:
    def __init__(self, codigo, cliente, carro, data_inicio, data_fim, status):
        self.codigo = codigo
        self.cliente = cliente
        self.carro = carro
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status

    def exibir(self):
        print("===== RESERVA =====")
        print(f"Código: {self.codigo}")
        print(f"Cliente: {self.cliente}")
        print(f"Carro: {self.carro}")
        print(f"Data início: {self.data_inicio}")
        print(f"Data fim: {self.data_fim}")
        print(f"Status: {self.status}")