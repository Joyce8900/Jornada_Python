import string
import random


senha_tamanho = int(input("Qual o tamanho da senha?"))
aleatorio =  (random.choice(string.ascii_letters))

senha = []
for i in range (0, senha_tamanho):
  senha.append(random.choice(string.ascii_lowercase))
  
print ("".join(senha))
##join junção da lista, por "", nesse caso por nada.