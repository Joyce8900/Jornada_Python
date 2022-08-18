# Criação de tuplas
# lista = [5,6,7]
# tupla= (1,2,3)
# tupla_2 = tuple(lista)
# print (type (tupla_2))
# print (tupla_2)
# tupla3= (1,)
# print (type(tupla3))

# Indexação
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"O quinto elemento é: {tupla[4]}")

# Indexação Negativa
print(f"O ultimo elemento da tupla é : {tupla[-1]}")

#Slicing (fatiamento)
tupla_slicing = tupla[4:]
print(tupla_slicing)

# Tentativa de alteração
#tupla[0] = 1

# Deleção com del
#del tupla [0]
# del tupla
# print(tupla)

# Métodos
print(f"A quantidade de elementos iguais é 1 : {tupla.count(1)}")
print(f"O elemento 10 está na posição: {tupla.index(10)}")

#Interação
for elemento in tupla:
    print (f"Elemento = {elemento} ")