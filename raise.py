#Nomes, idade, cargo
from ast import Pass


cadastro_csv= [
    "João, 28i,Analista de Sistemas",
    "Maria, 31,Desevolvedora Frontend",
    "Jonas, 37,Gerente de Projetos",
    "Alberto, 47"

]
def processa_dados(cadastros):
    for cadastro in cadastros:

        dados = cadastro.split(",")
        if len(dados)!=3:
            raise ValueError("Formato incorreto de dados")
        nome = dados [0]
        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError("Erro de formato de dado 'Idade'.")
        cargo = dados [2]
        print(f"{nome} tem {idade} anos e exerce o cargo de {cargo}")



try:
    processa_dados(cadastro_csv)
except ValueError as erro:
    print (f"O programa encontrou um erro. {erro}")