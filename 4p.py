#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).
a=eval(input("dati primul numar: "))
b=eval(input("dati al doilea numar: "))
for x in range (a, b+1):
    if (x%2!=0):
        print(x, end="")