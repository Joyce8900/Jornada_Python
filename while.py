from random import randint


Capacidade_Maxima_Balde = 1000
balde = 0
while balde <= Capacidade_Maxima_Balde:
    volume_copo = randint(95,100)
    print (f"O copo foi enchido com {volume_copo}ml")
    balde+= volume_copo
    print (f"O volume do balde é de {balde}ml")
print (f"O balde foi enchido com {balde}ml")