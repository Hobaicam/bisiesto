y = input("Introduce un año entre 1900 y 2199: ")
if int(y) < 1900 or int(y) > 2199:
    y = input("Error. Introduce un año entre 1900 y 2199: ")

bisiestos = int(y) - 1900
resta = int(y) - 1900
contador = 1900

if int(y)<1904 and int(y)>1899:
    print(f"La cantidad de años bisiestos entre 1900 y {y} es: {0} años.")
else:
    for x in range(1900, int(y)):
        if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
            bisiestos -= 1
    print(f"La cantidad de años bisiestos entre 1900 y {y} es: {(resta - bisiestos)+1} años.")