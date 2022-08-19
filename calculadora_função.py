def adicao(*numeros):
    return int(numeros[0]) + int(numeros[1])


def subtracao(*numeros):
    return int(numeros[0])-int(numeros[1])


def mutiplicacao(*numeros):
    return int(numeros[0])*int(numeros[1])


def divicao(*numeros):
    return int(numeros[0])/int(numeros[1])


numero_1 = (input("Digite o primeiro número:"))
operacao = input("Digite a operação: (- + / *)")
numero_2 = (input("Digite o segundo número:"))

if (numero_1.isnumeric()) == False:
    print(f"Primeiro número está inválido: '{numero_1}")
elif (numero_2.isnumeric()) == False:
    print(f"Segundo número está inválido: '{numero_2}'")
else:
    if operacao in "*/+-":
        if operacao in "+":
            resultado = adicao(numero_1, numero_2)
        elif operacao in "-":
            resultado = subtracao(numero_1, numero_2)
        elif operacao in "*":
            resultado = mutiplicacao(numero_1, numero_2)
        else:
            resultado = divicao(numero_1, numero_2)
        print(resultado)
    else:
        print(f"Operação inválida: '{operacao}'")