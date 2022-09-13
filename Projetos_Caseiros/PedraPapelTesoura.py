##Pedra, Papel e Tesoura
import os
print ("Bem vindo ao jogo!")
play1 = input("Escolhar a sua opção (Pedra, Papel ou Tesoura):").lower()
os.system('clear')
play2 = input("Escolhar a sua opção (Pedra, Papel ou Tesoura):").lower()
if (play1== "pedra"):
  if (play2== "pedra"):
    print ("Empate")
  elif (play2=="tesoura"):
    print ("Play1 GANHOU!")
  else:
    print ("Play2 GANHOU!")
elif (play1=="tesoura"):
  if (play2 == "pedra"):
    print ("Play2 GANHOU!")
  elif (play2=="tesoura"):
    print ("EMPATE!")
  else:
    print ("Play1 GANHOU!")
elif (play1=="papel"):
  if (play2== "pedra"):
    print ("Play1 GANHOU!")
  elif (play2=="tesoura"):
    print ("Play2 ganhou")
  else:
    print ("Empate")


