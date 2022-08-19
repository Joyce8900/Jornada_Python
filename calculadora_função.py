def adicao (numero1,numero2):
    return (numero1+numero2)


def subtracao (numero1,numero2):
    return numero1-numero2


def mutiplicacao (numero1,numero2):
    return numero1*numero2


def divicao (numero1,numero2):
    return numero1/numero2


numeros_operacao =  input("Digite os numeros que serão utilizados na operação, separando-os por espaço:").split(" ")
operacao = input("Digite a operação: (- + / *)")

if len (numeros_operacao) !=2:
    print ("Invalida!")
else:
    if operacao in "*/+-":
        if operacao in "+":
            resultado = adicao
            print (resultado)
        elif operacao in "-":
            resultado = subtracao
            print (resultado)
        elif operacao in "*":
            resultado = mutiplicacao
            print (resultado)
        else:
            resultado = divicao
            print (resultado)
