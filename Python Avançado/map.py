def trata_texto (txt):
  return txt.replace("'","").strip()


cadastros = {
"João, 18,joao@'mail.com    ",
"Joana, 22, joana@gmail.com '  ",
"Kléber, 24, kleber111@hotmail.com"
}


teste = map(trata_texto ,cadastros)

lista = list(teste)

print (lista)
