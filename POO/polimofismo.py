from random import randint
from time import sleep
from tkinter import N


valor_pedagio_carro = 3.5
valor_pedagio_moto = 2.75
valor_km_rodado_carro = 1.5
valor_km_rodado_moto = 1.25
class Automovel:
    numero_total_locacao = 0
    def __init__(self,montadora,modelo,alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente= ""
        print(f"Automovel {self.montadora} {self.modelo}, foi adquirido pela locadora!")
    

    def alugar(self, nome_cliente):
        Automovel.numero_total_locacao = Automovel.numero_total_locacao +1
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f"O automovel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}!")

    def devolver_automovel(self):
        self.alugado = False
        print(f"O automovel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}!")
        
        

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError

    @classmethod
    def mostrar_numero_total_locacoes(cls):
        print (f"Numero total de locações: {cls.numero_total_locacao}.")


class Carro(Automovel):
    numero_total_locacao_carro = 0
    valor_total_locacoes = 0
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print(f"O automovel comprado foi um carro {self.modelo}!")

    def alugar(self, nome_cliente):
        super(Carro, self).alugar(nome_cliente)
        Carro.numero_total_locacao_carro +=1


    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = (numero_pedagios*valor_pedagio_carro) +(valor_km_rodado_carro*km_rodados)
        print(f"Fatura do carro {self.montadora} {self.modelo} gerada com sucesso! Valor de R$:{self.valor_fatura:.2f}")
        Carro.valor_total_locacoes = Carro.valor_total_locacoes + self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacao != 0:
            media_locacoes = cls.valor_total_locacoes/cls.numero_total_locacao_carro
            print(f"Valor média de locação de carros é R$: {media_locacoes}/locação")
        else:
            print ("Número total de locação é zero.")

class Moto(Automovel):
    numero_total_locacao_moto = 0
    valor_total_locacoes = 0

    def __init__(self, montadora, modelo, alugado):
        super(Moto,self).__init__(montadora, modelo, alugado)
        print(f"O automovel comprado foi uma moto {self.modelo}!")

    def alugar(self, nome_cliente):
        super(Moto, self).alugar(nome_cliente)
        Moto.numero_total_locacao_moto += 1


    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = (numero_pedagios*valor_pedagio_moto) + (valor_km_rodado_moto*km_rodados)
        print(f"Fatura da moto {self.montadora} {self.modelo} gerada com sucesso! Valor de R$:{self.valor_fatura:.2f}")
        Moto.valor_total_locacoes+= self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacao != 0:
            media_locacoes = cls.valor_total_locacoes/cls.numero_total_locacao_moto
            print(f"Valor média de locação de moto é R$: {media_locacoes}/locação")
        else:
            print ("Número total de locação é zero.")





def mostrar_fatura(automovel):
    print(f"O valor da fatura do automovel {automovel.montadora} {automovel.modelo} alugado por {automovel.nome_cliente}"
    f", ficou no valor de R$:{automovel.valor_fatura:.2f}")

#-------------------------------------------------------------------------------------------------------------------------------------------------#

# fiesta = Carro("Ford", "Fiesta", False)
# fiesta.alugar("Pedro")

# #Simulação do tempo de aluguel
# sleep(randint(3,5))
# fiesta.devolver_automovel()
# fiesta.gerar_valor_fatura(numero_pedagios=5,km_rodados=750)
# mostrar_fatura(fiesta)
# honda = Moto("Honda", 150, False)
# honda.alugar("Pedro")
# sleep(randint(3,5))
# honda.devolver_automovel()
# honda.gerar_valor_fatura(numero_pedagios=0, km_rodados=150)
# mostrar_fatura(honda)


# fiesta = Carro("Ford","Fiesta",False)
# fiesta.alugar("Joyce Oliveira dos Santos")
# print(Carro.numero_total_locacao_carro)
# fiat_mobi = Carro("Fiat","Mobi",False)
# fiat_mobi.alugar("Joyce")

# print(Carro.numero_total_locacao_carro)
