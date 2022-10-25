emails = [
  "joyce.santos.709@ufrn.edu.br   , ",
  "JoyceSantos8900@hotmail.com ",
  "joycesantos8900@gmail.com             "
]

emais_tratados = [email.strip().replace(",", "").lower() for email in emails]
emais_tratados_gmail = [email.strip().replace(",", "").lower() for email in emails if "gmail" in email]


#print (emais_tratados)
#print (emais_tratados_gmail)


#Multiplos comum de 4 e 5
from random import randint

resultado =  [numero for numero in range(randint(0,501)) if numero %4 == 0 and numero %5 ==0]
print (resultado)