#           MODOS DE ABERTURA DE ARQUIVOS
#                   |   TEXTO   |   BINÁRIO
#-------------------------------------------------
#  LEITURA          ||    "r"   ||      "rb"
#  LEITURA/ESCRITA  ||    "r+"  ||      "rb+"
#-------------------------------------------------
#  ESCRITA          ||    "w"   ||      "wb"
#  ESCRITA/LEITURA  ||    "w+"  ||      "ab+"
# ------------------------------------------------
#   ANEXAR          ||    "a"   ||      "ab"
#   ANEXAR/LEITURA  ||    "a+"  ||      "ab+"
#





texto = "\n\nVenha lutar!"

arquivo = open("/home/aluno/Downloads/test.py\\dados.txt","r")
#Open: Abre arquivo


#arquivo.write(texto)
#Write: Escreve no arquivo
arquivo.close()
#close: fecha arquivo