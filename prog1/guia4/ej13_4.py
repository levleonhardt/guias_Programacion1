#Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez) y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).

lista_nom_ap = []

nombre = input("Ingrese nombre: ")
lista_nom_ap.append(nombre)
apellido = input("Ingrese apellido: ")
lista_nom_ap.append(apellido)
print(lista_nom_ap)
lista_nom_ap_inv = [0 for x in range(2)]
for i in range(len(lista_nom_ap)):
    a = lista_nom_ap_inv[i] = lista_nom_ap[-i+1]
for i in range(len(lista_nom_ap)):
    print(lista_nom_ap_inv[i], sep)
