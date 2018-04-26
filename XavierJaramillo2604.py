#Xavier Jaramillo
#Ejercicio en Clase 2604

print("Xavier Jaramillo")

numero=input("Ingrese su numero de cedula para procededer a sumar sus digitos\n")
suma=0
for cifra in numero:
    suma+=int(cifra)
    print(suma)