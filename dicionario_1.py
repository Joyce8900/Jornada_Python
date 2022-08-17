# computador ={
#     "cpu": "Xeon 79",
#     "ram": "DDR3 16gb",
#     "hdd": "Sansung 500gb",
#     "gpu": "GTX 750ti 2gb",
    
# }
# print (f"Computador V1:{computador}")
# computador ["ram"] = "4gb"
# print (f"Computador V2:{computador}")
# computador ["fonte"] = "Fonte 450w"
# print (f"Computador V3: {computador}")
# computador.update({"fonte":"400w","hdd":"Samsung 500gb + 500gb"})
# print (f"Computador V4: {computador}")
fila={
    "0": "João",
    "1": "Joyce",
    "2": "Arthur",
    "3": "Joelma",
    "4": "Pedro"


}
print (f"Fila 1: {fila}")
#del
del fila ["0"]
print (f"Fila 2: {fila}")
#pop
fila.pop("1")
print (f"Fila 3:{fila}")
#popitem (Retira o ultimo valor do dicionario)
valor_retirado = fila.popitem()
print (f"Fila 4:{fila}")
#clear (limpar tudo)
fila.clear()
print (f"Fila 5:{fila}")
