# Recursion je Rekurzija. Rekurzija je u matematici i računarstvu metoda
# definiranja funkcija u kojima se definirajuća funkcija primjenjuje unutar definicije. 
# Naziv se općenitije rabi za opis procesa ponavljanja objekata na samosličan način.
# Primjerice, kada su površine dvaju zrcala gotovo uzajamno paralelne,
# ugniježđene slike koje se pojavljuju su oblik rekurzije.

def tri_recursion(k):
    if (k > 0):
        result = tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(12)