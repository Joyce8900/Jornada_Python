#Iteravel 



lista = [1,2,3,4,5]

iterador_lista = iter(lista)

#print (next(iterador_lista))

class NumerosPares:
    def __init__(self, maximo):
        self.maximo = maximo
        self.atual = 0 
    
    def __iter__ (self):
        return self

    def __next__ (self):
        if self.atual > self.maximo:
            raise StopIteration
        
        retorno = self.atual

        self.atual += 2
        return retorno

iterador_pares = NumerosPares(maximo=150)
#for numero in iterador_pares:
    #print (numero,end = " ")




class NumerosPares:
    def __init__(self, maximo):
        self.maximo = maximo
        self.atual = 0 
    
    def __iter__ (self):
        return self

    def __next__ (self):
        if self.atual > self.maximo:
            raise StopIteration
        
        retorno = self.atual

        self.atual += 2
        return retorno

iterador_pares = NumerosPares(maximo=150)
for numero in iterador_pares:
    print (numero,end = " ")

#Geradores

def numeros_pares(maximo):
    atual = 0 
    while atual < maximo:
        yield atual
        atual += 2 



gerador_pares = numeros_pares(maximo=150)
for numero in gerador_pares:
    print (numero,end = " ")
