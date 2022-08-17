
homens ={"João","Pedro", "Joaquim","Rodrigo", "José", "Gabriel"}
alta_renda = {"Ana","Joyce","Pedro","João","José"}

print (f"Conjuntos dos homens: {homens}")
print (f"Conjunto de alta renda: {alta_renda}\n {'-' *84}\n")

#INTESEÇÃO
#Itens que estão em ambos os conjuntos.
homens_alta_renda = homens.intersection(alta_renda)
print (f"Usuarios homens com alta renda são:\n {homens_alta_renda}\n")

#UNIÃO
#Itens de ambos os conjuntos.
homens_e_alta_renda = homens.union(alta_renda)
print (f"Homens e usuários com alta renda: \n{homens_e_alta_renda}")

#DIFERENÇA
#Itens que estão apenas em um dos conjuntos.
homens_nao_alta_renda = homens.difference(alta_renda)
alta_renda_nao_homens = alta_renda.difference(homens)
print (f"Homens sem alta renda :\n {homens_nao_alta_renda}")
print (f"Usuários alta renda sem homens:\n {alta_renda_nao_homens}")

#DIFERENÇA SIMÉTRICA
#Itens que estão em um conjunto ou em outro mas não em ambos.
homens_nao_alta_renda_e_mulheres = homens.symmetric_difference(alta_renda)
print (f"Homens não alta renda, e mulheres alta renda: \n{homens_nao_alta_renda_e_mulheres}")

#MÉTODOS DE CONJUNTOS
print(f"Os conjuntos Homens e Alta Renda são disjuntos? {(homens.isdisjoint)}")
#ISDISJOINT verifica os conjuntos não tem inteseção entre eles.
print(f"O conjunto de homens é um subconjunto de alta renda?\n{(homens.issubset(alta_renda))}")
#ISSUBSET verificar se todos os elementos de um conjunto está contido no outro conjunto.
print(f"O conjunto de homens é um superconjunto de alta renda? \n {(homens.issuperset(alta_renda))}.")

#Interseção
print (homens & alta_renda)
#União
print (homens | alta_renda)
#Diferença
print(homens - alta_renda)
#Diferença Simétrica
print (homens ^ alta_renda)
