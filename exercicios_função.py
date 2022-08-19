#1. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
def reverte (digito):
    return (digito.reverse())

# def validarNumero (numero):
#     if (numero.isnumeric()) == False:
#         print ("Digite apenas números!")
#     else:
#         return True


# numero = input("Digite um número inteiro:")
# list = [numero]














#2.Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 

def quantidade (numero):
    return (len(numero))


teste = (input("Digite um número inteiro:"))

resultado =  quantidade(teste)

if (teste.isnumeric()) == False:
    print ("Digite apenas números!")
else:
    print (int(resultado))

