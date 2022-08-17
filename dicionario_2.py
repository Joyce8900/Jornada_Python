from tkinter import E


familia = {
    "pai":"João Pereira",
    "mãe": "Joelma Oliveira",
    "namorado":"Pedro Sérgio"
}
print (f"Familia:{familia}")

#Copy
#Copia dicionario
copia_familia= familia.copy()
print(f"Cópia Familia:{copia_familia}")

#ITEMS
#Retorna os pares  chaves: valor os formato de lista

itens = familia.items()
for item in familia.items():
    print(f"\t Chaves = {item[0]} e valor = {item[1]}")

#Keys
#Retorna tododas as chaves em formato de lista
chaves = familia.keys()
print (f"Keys: {chaves}")
for chave in chaves:
    print (f"\t Chave: {chave}")

#VALUES
#Retorna todos os valores em formato de lista
valores = familia.values()
print (f"Valores: {valores}")
for valor in valores:
    print (f"\t Valor: {valor}")

#SETDEFAULT
#Insere a chave como valor passado SE a chave não estiver presente no dicionario
#Retorna o valor da chave SE a chave já estiver presente no dicionario.

familia.setdefault("sobrinho", "Arthur")
familia.setdefault("mãe","Joelma Oliveira")
print (familia)

#FRONKEYS
#Cria um dicionario a partir de uma lista de chaves e de valor

chaves = ["mae","pai","filha"]
jogo = dict.fromkeys(chaves, 0)
print (jogo)