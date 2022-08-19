numeros = float(input(print("Digite o primeiro número:")))
operacao = input(print("Digite a operação"))
numero2 = float(input(print("Digite o segundo número:")))
equacao = f"{numeros} {operacao} {numero2}"
resultado = eval(equacao)
print(f"{' ' * 20 }\nResultado:{resultado}  {' '*20}\n")
