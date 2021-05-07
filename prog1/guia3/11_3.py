#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.
from datetime import *

lista_nombres = []
fechas_nacimiento = []

nombre=''
while nombre != "0":
    nombre = input("Insertar nombre (0 para cancelar): ")
    lista_nombres.append(nombre)

for i in range(len(lista_nombres)):
    

anio = int(input('Ingrese año: '))
mes = int(input('Ingrese mes: '))
dia = int(input('Ingrese día: '))
fecha = datetime.date(anio, mes, dia)