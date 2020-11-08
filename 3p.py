#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele pare, pentru intervalul de la 1 la n (n-este citit de la tastatură).
n=eval(input("dati numarul: "))
for a in range (0, n+1, 2):
    print(a, end="")