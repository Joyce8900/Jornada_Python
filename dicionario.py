cadastro = {
    "id": 1, 
    "nome": "Pedro Sérgio Bezerra",
    "CPF": 70957526482,
    "Tel": 84999271376,
    "filhos": ["Maria","Junior"],
    "compras": [
        {
            "id":463,
            "produto": "Notebook Acer",
            "preco": 2999.99
        },
        {
            "id": 587,
            "produto": "Monitor Gamer 24 polegadas",
            "preço": 999.00
        },
    ]
}
filhos = cadastro.get("filhos")

notebook_gamer = cadastro["compras"] [0] ['produto']
nome = cadastro.get("nome")
# print (filhos)
# print (f"O usuario {nome}, fez a seguinte compra {notebook_gamer}")
# print (type(cadastro["compras"]))
# print (type(cadastro["compras"][1]))
#print (f"O usuario {cadastro['nome']}, realizou a seguinte compra: {cadastro['compras'][1]['produto']}")
#print (f"O usuario {cadastro['nome']}, realizou a seguinte compra: {notebook_gamer}")
