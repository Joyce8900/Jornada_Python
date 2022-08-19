# def funcao_args (arg1, arg2,*args):
#     print (f"Arg1: {arg1}")
#     print (f"Arg2: {arg2}")
#     print (f"Args: {args}")


# funcao_args(1,2,3,4,5,6,8,7,0,8,9)
def soma (maximo,*numeros):
    resultado = 0
    numeros_somados = []
    for numero in numeros:
        if (resultado + numero > maximo):
            break

        resultado+=numero
        numeros_somados.append(numero)

    return resultado,numeros_somados
  
#Nessa função foi feito um if para limitar o resultado a 100
#numero_somados.append(numeros) recebe todo elemento numero, e amazenar para depois exibir.

resultado_final, numeros_somados= soma (100,8,9,80)
print (resultado_final)
print (numeros_somados)
