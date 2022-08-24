# 1. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
import math


def reverte(num):
    return print(str(num)[::-1])


# Usando o conceito de fatiamento de string, você pode reverter a string. ::-1corresponde a start:stop:step.
# Quando você passa -1 como step, o startponto vai para o final e stopna frente.

numero = int(input("Digite um número inteiro:"))
go = reverte(numero)


# 2.Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def validarN(numero):
    if (numero.isnumeric()) == False:
        print(f"Digite apenas números! {numero}")
        return (len(numero))
    else:
        return print(len(numero))


teste = (input("Digite um número inteiro:"))

resultado = validarN(teste)

# 3. Faça uma função que computa a potência a**b para valores a e b
# (assuma números inteiros) passados por parâmetro (não use ooperador **).


def potencia(a, b):
    return print(pow(a, b))


n1 = int(input("Valor da base:"))
n2 = int(input("Valor da base:"))

resultado = potencia(n1, n2)


# 4. Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja um prefixo da segunda.
# Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ não é prefixo de ’uf’.
def verificarP(frase, palavra):
    if (frase.count(palavra)) == 0:
        return print(False)
    else:
        return print(True)


f = ("O céu está lindo hoje!")
p = ("lindo")
G = verificarP(f, p)


# 5.Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.
def descontos(inicial, porcentagem):
    desconto = float(inicial * (porcentagem/100))
    fim = float(inicial+desconto)
    return print(f"Valor total: {fim}reais")


valor1 = float(input("Qual o valor da conta:"))
menos = float(input("Qual a porcentagem da gorjeta:"))

total = (descontos(valor1, menos))
