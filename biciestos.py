y=input("Introduce un año entre 1900 y 2199: ")
while int(y) <1900 or int(y) > 2199:
    y=input("Error. Introduce un año entre 1900 y 2199: ")
bisiestos=int(y)-1900

contador=1900
while contador+1<int(y):  
    if int(contador)%4==0:
        if int(contador)%100==0 and int(contador)%400 != 0:
            contador+=1
            bisiestos-=1
            
        else:
           
            contador+=1
    else:
        contador+=1
        bisiestos-=1

 

print(f"La cantidad de años bisiestos entre 1900 y {y} es: {bisiestos} años.")
    
