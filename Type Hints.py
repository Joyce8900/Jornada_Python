##Dicas de Tipos
def aplicar_baskhara(a:float,b:float,c:float)->(float):
    delta = b**2-4*a*c
    x_1 = (-b+(delta**1/2))/(2*a)
    x_2 = (-b-(delta**1/2))/(2*a)
    return x_1, x_2


def aplicar_desconto(produtos: dict,desconto:float)->dict:
    resultado = {}
    for nome_produto, valor in produtos.items():
       resultado[nome_produto] = f"{valor *(1 - desconto):.2f}"
    return resultado



valores_de_produtos={
    "Macarrão": 4.66,
    "Feijão": 8.99,
    "Carne": 39.99
}

#print (aplicar_desconto(valores_de_produtos,0.15))
print (aplicar_baskhara(5,15,-25))
