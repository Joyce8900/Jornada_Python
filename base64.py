import base64
##Transforma imagem para binario.

with open ("./labens.png",'rb') as arquivo:
  arquivo_b64 = base64.b64encode(arquivo.read())
  print (arquivo_b64)