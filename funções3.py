def soma(numero_1,numero_2):
    return numero_1+numero_2


resultado_1 = soma(10,20)
resultado_2 = soma(1,50)
# print (resultado_1)
# print (resultado_2)

def calculado_media_mediana(notas):
    media = sum(notas)/len(notas)
    mediana = 0
    if len(notas)%2 == 0:
        #numero par de elementos
        indice_ponto_central_menor = int(len(notas)/2-1)
        indice_ponto_central_maior = int(len(notas)/2)
        ponto_central_menor = notas[indice_ponto_central_menor]
        ponto_central_maior = notas[indice_ponto_central_maior]
        mediana =(ponto_central_menor + ponto_central_maior)/2
        pass
    else:
        #numero impar de elementos
        notas_ordem = sorted(notas) ##sorted ordena a lista.
        indice_mediana = int(len(notas)/2)
        mediana = notas_ordem[indice_mediana]


    return media,mediana


##sum soma todos os elementos da lista
##len informa a quantidade de itens da lista.

resultado_media,resultado_mediana = calculado_media_mediana([6,6,6,6])
print (resultado_media)
print (resultado_mediana)
