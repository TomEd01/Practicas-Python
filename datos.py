'''
            VARIABLES
    °No pueden empezar con numeros pero si con gion bajo (en casos especiales)
    °Solo pueden contener caractares afanumericos (A-Z,a-z,0-9,_)
    °Se distingue entre mayuscula y minuscula
'''
print('\n')
edad = 24 #Tipo de dato entero
Edad = 19
EDAD = 33
print(type(edad))
print(edad,Edad,EDAD)
#-----------------FLOTANTE--------------#
print('\n')
flo = 5.5 #Tipo de dato flotante = decimal
print(type(flo))
print(flo)
#-----------------STRING---------------#
print('\n')
nombre = 'Edwin Tomas / TomiCat' #Tipo String = cadena de caracteres
print(type(nombre))
print(nombre)
#----------------BOOLEANO--------------#
print('\n')
bo = True #Tipo de dato boleano
print(type(bo))
print(bo)
#-----------ARRAY // LISTA--------------#
print('\n') #Datos que se modifican
lista = [10,20,30,40]
lista_combinada=[nombre,edad,True,flo]
print(type(lista))
print(lista_combinada)
#----------Tuples----------------------#
print('\n')#Datos que no cambian / no es mutable
tupla=(1,2,3,4)
tupla_vacia=()
print(type(tupla))
print(tupla)
#----Directories / Api / Objeptos-----#
print('\n')
print(type({
    "Nombre":"Daniel",
    "Apellido":"López"
}))
print({
    "Nombre":"Daniel",
    "Apellido":"López"
})