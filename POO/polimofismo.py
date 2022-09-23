valor_pedagio_carro = 3.5
valor_pedagio_moto = 2.75
valor_km_rodado_carro = 1.5
valor_km_rodado_moto = 1.0
class Automovel:
    def __init__(self,montadora,modelo,alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente= ""
        print(f"Automovel {self.montadora} {self.modelo}, adquirido pela locadora!")
    

    def alugar(self, nome_cliente):
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f"O automóvel {self.montadora} {self.modelo} foi alugado para {self.nome_cliente}")

    def devolver_automovel(self):
        self.alugado = False
        self.nome_cliente = ""
        print(f"O automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}")

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError


class Carro(Automovel):
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios*valor_pedagio_carro + valor_km_rodado_carro
        print(f"Fatura do carro {self.montadora} {self.modelo} gerada com sucesso! Valor de R$: {self.valor_fatura}")

class Moto(Automovel):
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios*valor_pedagio_moto + valor_km_rodado_moto
        print(f"Fatura da moto {self.montadora} {self.modelo} gerada com sucesso! Valor de R$: {self.valor_fatura}")