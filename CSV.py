"""
1) Ler arquivo de entrada CSV
2) Processamento (Retirada do campo ID e junção do campo NOME e SOBRENOME)
3) Gravação do arquivo de CSV de saída.

"""
resultados = []
with open ("./dados.csv", "r") as arquivo_entrada:
  linhas = arquivo_entrada.readlines()[1:]
  for linha in linhas:
    dados = linha.split(",")
    email = dados[3].replace(f"\n"," ")
    resultados.append(f"{dados[1]} {dados[2]}, {email}\n")
  


with open ("./dados_cadastro.csv", "w") as arquivo_saida:
    for resultado in resultados:
        arquivo_saida.write(resultado)
 