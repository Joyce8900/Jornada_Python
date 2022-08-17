#for : sintaxe basica



sequencia = [1,2,3]
for elemento in sequencia:
   print (f"{elemento}")

#Print de cada elemento de sequencia.

#Range
# for (i=0; i<= 10; i=+2)
for i in range(0,10+1,2):
    print (f"O valor de i é {i}")
#Modelo de for em print.

# Iterando sobre Estruturas de Dados
set_ = {1,2,3}
tupla = (1,2,3)
lista = [1,2,3]
dicionario = {"a":1,"b":2}

for elemento in set_:
    print(f"[SET] Elementos do set: {elemento}")
for elemento in tupla:
    print(f"[TUPLA] Elemento da tupla: {elemento}")
for elemento in lista:
    print (f"[LISTA] Elementos da lista: {elemento}")
for elemento in dicionario.items():
    print (f"[DICIONARIO] Elementos do dicionarios: {elemento} ")