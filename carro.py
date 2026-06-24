class Esportivo(Carro):
    def __init__(
        self,
        placa,
        ano,
        cor,
        modelo,
        quilometragem,
        valor_diaria,
        observacao,
        tempo_100_milhas,
        melhorias
    ):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao)
        self.tempo_100_milhas = tempo_100_milhas
        self.melhorias = melhorias

    def exibir(self):
        super().exibir()
        print("Categoria: Esportivo")
        print(f"Tempo até 100 milhas/h: {self.tempo_100_milhas}")
        print(f"Melhorias: {self.melhorias}")


class Importado(Carro):
    def __init__(
        self,
        placa,
        ano,
        cor,
        modelo,
        quilometragem,
        valor_diaria,
        observacao,
        quantidade_passageiros,
        tamanho_bagageiro,
        km_por_litro
    ):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diaria, observacao)
        self.quantidade_passageiros = quantidade_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_por_litro = km_por_litro

    def exibir(self):
        super().exibir()
        print("Categoria: Importado")
        print(f"Quantidade de passageiros: {self.quantidade_passageiros}")
        print(f"Tamanho do bagageiro: {self.tamanho_bagageiro}")
        print(f"Km por litro: {self.km_por_litro}")