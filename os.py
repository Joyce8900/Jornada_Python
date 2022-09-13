import os
os.mkdir("./Nova Pasta")
##Criar Pasta

for diretorio in os.listdir("./"):
  print (diretorio)
##Print de todos os diretorios da pasta.
##------------------------------------------##
if os.path.exists("./Nova Pasta[2]"):
  print ("\'Nova Pasta já existe'")
else:
  os.mkdir("./Nova Pasta[2]")


##Verificar pasta existente
##----------------------------------------##

os.rmdir("./Nova Pasta[2]")

## Excluir Pasta
##---------------------------------------##
print (os.getcwd())
##Printa o caminho que está sendo utilizado
##---------------------------------------##
os.rename("./labens.png", "logo-labens.png")
##Renomear pasta ou arquivo
#----------------------------------------##
print (os.path.getsize("./logo-labens.png"))
#Determina o tamanho do arquivo
#---------------------------------------##