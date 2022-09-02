def divisao_de_dois_numeros (dividendo:float,divisor:float)->(float):
    return (f"{(dividendo/divisor):.2f}")


numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
resultado = divisao_de_dois_numeros(numero1,numero2)
print (resultado)
