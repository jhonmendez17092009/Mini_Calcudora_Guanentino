# input
import math
print("selecine una operacion")
print("1 sumar")
print("2 restar")
print("3 multiplicar")
print("4 dividir")
print("5 potencia")
print("6 logaritmo")

opc = int(input("digite el numero de la operacion"))
x = int(input("ingrese un numero"))
y = int(input("ingrese un numero"))

if opc == 1:
    r = x+y

if opc == 2:
    r = x-y

if opc == 3:
    r = x*y

if opc == 4:
    r = x/y

if opc == 5:
    r = x^y

if opc == 6:
    r = math.log(x,y)

#output
print("resultado: "+str(r))