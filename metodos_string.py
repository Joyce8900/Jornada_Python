print ("   Strip   " .strip()) 
print ('maiusculo'.upper()) 
print('MINÚSCULO'.lower() ) 
print('T, exto, Com vá, ria,s v, ir,a, ulas'.replace(','," "))
print("Texto teste para função count".count('e')) 
print("Texto Centralizado".center(58,' '))
print('Avião?'.index('ã'))
print('10'.isnumeric())
print('Teste de quebra de string com split'.split(' '))
print('NOME;CIDADE; IDADE;PAIS;'.split(';')) 
print('este é um titulo'.title()) 
print('este é um titulo'.capitalize())
print('585'.zfill(5))

#Encadenamento de metodos
print ("       Tex;t;o ".strip().center(20,"_").replace(";","").upper())
#Tamanho de string
string_contador = "Esse é um teste realizado para contar a quantidade de strings de uma variavel."
print(len(string_contador))
print(string_contador[-1]== ".")