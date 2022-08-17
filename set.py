#Criando sets

lista = [1,2,3]
set_1 = {1,2,3}
# print (set_1)
# print (type(set_1))

set_2 = set(lista)
# print (set_2)

carteira= {"PETR4","CASH3", "MGLU3", "BBAS3","WEGE3"}
print (f"Carteira de inicial: {carteira}")

#ADD
#Adiciona novos elementos;
carteira.add("ITUB4")
print (f"Carteira v2:{carteira}")

#UPDATE
#Atualizar elementos com update, ele irá adicionar caso o elemento não estiver na set
carteira.update({"PETR4","ABEV3","RAIZ4"})
print (f"Carteira v3:{carteira}")

#DISCARD
#Remove elementos.
carteira.discard("PETR4")
print(f"Carteira v4:{carteira}")

#REMOVE
#Remove elementos, apresentaram um erro de tipo, caso o valor passado não esteja no set.
carteira.remove("RAIZ4")
print (f"Carteira v5: {carteira}")

#POP
#Remove o ultimo elementos(set não possui ordem então não é possivel saber qual item será removido)
item = carteira.pop()
print (f"Carteira v6:{carteira}")
print (f"Item removido: {item}")

#CLEAR
#Remover todos os elementos do set.
carteira.clear()
print(f"Carteira v7:{carteira}")
