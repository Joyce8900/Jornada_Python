from random import choice

class Desenvolvedor:
  def __init__(self, linguagens_programacao = None):
      self.linguagens_programacao= linguagens_programacao
      print(f"Novo Desenvolvedor com expertise nas linguagens: \n\t {self.linguagens_programacao}")
  def desenvolver_codigo(self):
    print(f"Psiu. Dev codando em {choice(self.linguagens_programacao)}")

class Gerente:
  def __init__(self, softkills= None):
      self.softkills = softkills
      print(f"Novo gente com habilidades nas SoftSkills: \n\t{self.softkills}")
  def gerenciar_equipe(self):
    print(f"Gerente está utilizando {choice(self.softkills)} para gerenciar sua equipe!")
class TechLead (Desenvolvedor,Gerente):
  def __init__(self, linguagens_programacao=None, softkills=None):
      Desenvolvedor.__init__(self,linguagens_programacao)
      Gerente.__init__(self,softkills)

TechLead = TechLead(["C","Python","C++","Ruby","go","Java","Javascript"], ["Liderança", "Comunicação Ativa", "Feedbacks"])
TechLead.desenvolver_codigo()
TechLead.gerenciar_equipe()