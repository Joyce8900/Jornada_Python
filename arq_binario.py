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



arquivo_png = open("/home/aluno/Downloads/36963223.png","rb")
retorno_png = arquivo_png.read()
arquivo_saida = open("/home/aluno/Downloads/labens.png","wb")
arquivo_saida.write(retorno_png)
arquivo_saida.close()
#close: fecha arquivo