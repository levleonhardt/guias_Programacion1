#Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.

texto = input("Ingrese un texto: ")
letra = input("Ingrese una letra para corroborar cuántas veces se repite: ")

repeticiones=0

if letra in texto:
    for i in range(len(texto)):
        if texto[i] == letra:
           repeticiones = repeticiones +1
    print("La letra se repite " + str(repeticiones) + " veces.")
else:
    print("La letra no se encuentra en el texto.")
