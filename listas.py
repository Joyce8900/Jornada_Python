# lista = []

# print(lista)
# print(type(lista))
# lista = list([])
# print(lista)
# print(type(lista))
# lista = [9, "Joyce", 6.8, [9, 6, "Santos"]]
# print(lista)

# for elemento in lista:
#     print(elemento)

# pares = [2, 4, 6, 8]
# impares = [1, 3, 5, 7]
# print(pares[0]*impares[0])
# print(pares[0]**impares[2])
# print(f"O segundo elemento da lista pares é {pares[2]}.")
# print(pares[-1]*impares[-1])
# print(pares[0])
# print(pares[1])
# print(pares[2])
# print(pares[3])
# print(pares[-1])
# print(pares[-2])
# print(pares[-3])
# print(pares[-4])

# print(pares[-5])
from random import randint


# alunos = ["João","Maria","Clara","José","Marcos","Pedro"]

# for aluno in alunos:
#     print(f"Nome do aluno: {aluno}")
# for aluno in alunos:
#     nota = randint (3,10)
#     print (f"{aluno} nota: {nota}")
# for aluno in alunos:
#     nota_1 = randint(5,10)
#     nota_2 = randint(4,8)
#     nota_3 = randint(2,7)
#     nota_final = (nota_1*0.2)+(nota_2*0.3)+(nota_3*0.5)
#     print (f"Aluno: {aluno}  nota: {nota_final}")
# alunos = ["João","Maria","Clara","José","Marcos","Pedro"]
# notas = [randint(5,10),randint(5,10),randint(5,10),randint(5,10),randint(5,10),randint(5,10)]
# for aluno,nota in zip(alunos,notas):
#     print(f"Aluno: {aluno} nota:{nota}")

              ##Slicing###

#           0   1   2   3   4   5
# letras =  ["a","b","c","d","e","f"]
#          -6  -5  -4  -3   -2  -1
# print (letras[0:3:1])
# print (letras[3:6:1])
# print (letras[::-1])
# print (letras [-6:-3:1])
# print (letras[::2]+letras[1::2])


#                      Manipulando lista           #

sacola = ["arroz","feijão","carne","farinha"]
print (f"Lista de inicial: {sacola}")

#Metodo APPEND (objeto)
#Adiciona um item no fim da lista.
sacola.append("Macarrão")
print (f"Lista após append(): {sacola}")

#Método: EXTEND(estrutura)
#É adicionado todos os itens de outra estrutura no fim da lista
sacola.extend(["Maionese","Ketchup"])
print (f"Lista após metodo extend(): {sacola}")

#Método INSERT(indice,objeto)
#informe um item na posição desejada
sacola.insert(0,"Milho")
print (f"Lista após metodo insert(): {sacola}")

#Metodo REMOVE (objeto)
#Remove o primeiro elemento igual ao valor passado
sacola.remove("Macarrão")
print (f"Lista após metodo remove(): {sacola}")

#Método POP (indice)
#Remove o item da posição desejada da lista e o retorna
#Caso o indice não seja especificado, retorna o último elemento
elemento = sacola.pop()
print (f"Lista após metodo pop(): {sacola}")
print (elemento)

#Método CLEAR()
#Remove todos os elementos da lista
# sacola.clear()
# print (f"Lista após metodo clear(): {sacola}")

#Método INDEX (valor[,começo,fim])
#Retorna o indice do primeiro elemento do valor especificado
#Podemos ainda passar outros dois parametros que dizem onde pesquisar na lista (começo e fim)
#print (sacola.index("farinha",0,6))
print (f"Lista após metodo index(): {sacola}")

#Metodo COUNT(valor)
#Conta o número de ocorrências do valor especificado na lista
print (sacola.count("arroz"))
print (f"Lista após metodo count(): {sacola}")

#Método SORT()
#Ordena os itens da lista. Parametros adiconais podem ser utilizados pata customizar a ordenando
#sacola.sort()
print (f"Lista após metodo sort(): {sacola}")

#Método REVERSE()
#Reverte os elementos da lista
sacola.reverse()
print (f"Lista após metodo reverse(): {sacola}")

#Método COPY()
# Retorna uma lista com a copia dos elementos da lista de origem
copy_sacola=sacola.copy()
print (f"Lista após metodo copy(): {copy_sacola}")