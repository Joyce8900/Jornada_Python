from datetime import datetime

class Empregado:
    numero_empregados = int
    def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario

    def iniciar_jornada(self):
        print (f"{self.nome_completo} de matricula {self.matricula_funcional}, iniciou sua jornada de trabalho {datetime.now()}")

    def fim_jornada (self):
        print (f"{self.nome_completo}, de matricula {self.matricula_funcional}, finalizou sua jornada as {datetime.now()})")
    def receber_aumento(self):
        raise NotImplemented

class Desenvolvedor(Empregado):
    porcentagem_salarial = 1.05
    def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int, linguagens: list, litros_cafe: float = 0.0, burnout: bool = False):

        super().__init__ (self, nome_completo,salario, email,salario)
        super().numero_empregados += 1

        self.linguagens = linguagens
        self.litros_cafe = litros_cafe
        self.burnot = False

    def Adicionar_linguagem(self, nova_linguagem: str):
        self.linguagens(self, nova_linguagem)
        print (f"Desenvolvedor {self.nome_completo}, aprendeu uma nova linguagem, essa linguagem é {nova_linguagem}!")
    def Beber_cafe(self, qtde_cafe: float):
        self.litros_cafe += qtde_cafe
        if (self.litros_cafe >=2):
            print (f"{self.nome_completo} de matricula {self.matricula_funcional}"
                    f"teve um burnot devido por consumi 2 ou mais litros de café, e com isso teve sua jornada encerrada mais cedo!")
            self.burnot = True
            self.fim_jornada()

    

class GerenteProjeto(Empregado):
    porcentagem_salarial = 1.5
    def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int, time:list, projetos_envolvidos: str):
        super().__init__(nome_completo, email, matricula_funcional, salario)
        super().numero_empregados += 1
        self.time = time
        self.projetos_envolvidos = projetos_envolvidos
    def AdicionarDev (self, dev: Desenvolvedor):
        self.time.append(dev)
        print (f"{dev.matricula_funcional} foi adicionado ao time do Gerente {self.nome_completo}")
    def remover_desenvolvedor(self, dev: Desenvolvedor):
        self.time.remove(dev)

        print(f'Desenvolvedor [{dev.matricula_funcional}] {dev.nome_completo} '
              f'foi removido do time do Gerente {self.nome_completo}.')

    def participar_projeto(self, novo_projeto: str):
        self.projetos_envolvidos.append(novo_projeto)

        print(f'O Gerente [{self.matricula_funcional}] '
              f'{self.nome_completo} participará do projeto {novo_projeto}!')

    def sair_projeto(self, projeto: str):
        self.projetos_envolvidos.remove(projeto)

        print(f'O Gerente [{self.matricula_funcional}] '
              f'{self.nome_completo} saiu do projeto {projeto}!')

    def receber_aumento(self):
        self.salario *= GerenteProjeto.porcentagem_aumento

        print(f'O Gerente [{self.matricula_funcional}] '
              f'{self.nome_completo} recebeu um aumento! Parabéns!')
