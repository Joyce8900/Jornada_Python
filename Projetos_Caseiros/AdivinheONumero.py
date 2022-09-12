from random import randint
numero = randint (10,101)
print ("Bem vindo ao Jogo de Adivinhe o número!")
n = int(input("Digite o numero:"))
while (numero != n):
  if n > numero:
    n = int(input(f"Seu número é maior. Digite outro número:"))
  elif n<numero:
    n = int(input(f"Seu número é menor. Digite outro número:"))
print (numero)
    
