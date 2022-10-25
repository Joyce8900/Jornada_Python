cadastros = {
"João, 18,joao@'mail.com    ",
"Joana, 22, joana@gmail.com '  ",
"Kléber, 24, kleber111@hotmail.com"
}


lista = list(map(lambda txt: txt.replace("'","").strip(), cadastros))
##print (lista)

resultado_filter =  list(filter(lambda cadastro : "gmail" in cadastro, lista ))

print(resultado_filter)