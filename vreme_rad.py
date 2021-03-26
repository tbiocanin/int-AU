import time as t 

def test_rat():

    print("Ovo cudo radi")

 


niz_vreme = t.localtime()
sat = niz_vreme.tm_hour
minut = niz_vreme.tm_min

while (minut != 21):
    if sat == 19 and minut == 18:
        test_rat()
    else:
        print("ne radi kod")