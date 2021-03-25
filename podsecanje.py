import time as t 

##vreme koje je proslo od pocetka koda do kraja koda, dobro je za proveravanje
def izr_proizvod():

    proizvod = 1
    for i in range (1, 10000):
        proizvod *= i 
    return proizvod
pocetak = t.time()
proizvod = izr_proizvod()
kraj = t.time()

print(pocetak)
print(kraj)
print(kraj-pocetak)