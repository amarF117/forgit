import random 

zamisnjeni_broj = random.randint(1,10)
broj_pokusaja = 0


for i in range(10):
    pogoceni_broj = int(input("molimo unesire broj"))
    broj_pokusaja = broj_pokusaja +1
    if (pogoceni_broj == zamisnjeni_broj):print("pogodili ste broj iz ",broj_pokusaja,"pokusaja")