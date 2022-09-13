
from random import randint
numero = randint (1,101)
print ("Bem vindo ao Jogo de Adivinhe o número!")
n = int(input("Digite o numero:"))
contado = 900
while (numero != n and contado<1000):
  if n > numero:
    n = int(input(f"Seu número é maior. Digite um número menor que {n}  :"))
    contado = contado+100
  elif n<numero:
    n = int(input(f"Seu número é menor. Digite um número maior que {n}  :"))
    contado=contado+100
if (contado==1000):
  print(f"Você já usou todas as suas 10 fichas, o número é {numero}")
else:
  print (f"Parabéns você acertou! {numero}")
    