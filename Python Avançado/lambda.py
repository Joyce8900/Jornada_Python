cadastros = {
"João, 18,joao@'mail.com    ",
"Joana, 22, joana@gmail.com '  ",
"Kléber, 24, kleber111@hotmail.com"
}


lista = list(map(lambda txt: txt.replace("'","").strip(), cadastros))
print (lista)
