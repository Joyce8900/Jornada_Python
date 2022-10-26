clientes ={
    "Joyce" : "709.575.264-82",
    "Maria": "325.377.670-04",
    "Pedro": "022.079.610-60",
    "João" : "656.633.250-26",
    "Karoline": "402.109.550-07"
}

# resultado = {}
# for chave, valor in clientes.items():
#     resultado [chave] = valor.replace(".", "").replace("-", "")
resultado = {chave.lower():valor .replace(".","").replace("-","") for chave, valor in clientes.items()}

#print (resultado)
salarios = {
  "Joyce": 1890,
  "Pedro": 2349,
  "Joelma": 2900
  }
salarios_maior_2000 = {chave:valor for chave ,valor in salarios.items() if valor >= 2000}

print (salarios_maior_2000)