#sacar la n-esima raiz

#vamo a importar un paketote (no es necesario tho)
import math

#funcion para sacar la n-esima raiz:

def N_raiz (num,raiz):
    output = num **(1/raiz)
    return output

#podemos usarlo al chingadazo:

resultado = N_raiz (16,2)
print (resultado)

#o podemos hacer una "interfaz":

#pedimos al usuario que introduzca los numeros usando la funcion integrada input:

VarNum1 = input("Intruduzca el numero:")
VarRaiz1 = input("Introduzca la raiz:")

#convertimos las entradas de string a float

VarNum1 = float(VarNum1)
VarRaiz1 = float(VarRaiz1)

#y llamamos la funcion

N_raiz (VarNum1 , VarRaiz1)

print(N_raiz(VarNum1 , VarRaiz1))