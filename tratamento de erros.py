def divisao_de_dois_numeros (dividendo:float,divisor:float)->(float):
    return (f"{(dividendo/divisor):.2f}")


try:
    ##Código a ser testado
    numero1 = float(input("Digite o primeiro número:"))
    numero2 = float(input("Digite o segundo número:"))

    resultado = divisao_de_dois_numeros(numero1,numero2)


    print (resultado)



except (TypeError,ZeroDivisionError) as excecao:
    print (f"Erro de tipo! Ou divisão por zero não suportada. Erro: {excecao}")

except Exception:
    #Execute esse código caso um erro ocorra
    print ("Erro")

else:
    #Execute esse código caso nenhum erro ocorra
    print (resultado)
finally:
    #Sempre execute esse código
    print ("Finalizando... Muito obrigada!")