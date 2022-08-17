idade = int(input(print("Qual sua idade?")))
sexo = input(print("Qual seu sexo? F(Feminino)   M(Masculino) "))
if sexo.upper() == "F":
    if idade >= 60:
        print ("Provado!")
    else:
        print (f'Negado! Faltam {60-idade} anos')

elif sexo.upper() == "M":
    if idade >=65:
        print ("Aprovado!")
    else:
        print (f"Negado! Faltam {65 - idade} anos")
    
else:
    print ("Sexo inválido!!")


