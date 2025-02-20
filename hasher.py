#!/usr/bin/python3

# Cifra un documento que reciba como parametros en hashes hexadecimales

import sys

# Copio todo y encripto después en un hash único, eliminar cuanto antes la copia por seguridad luego de escribir al archivo
lectura = open(sys.argv[1].__str__(), 'r')

copia = ''
# Cifro las lineas con hashes positivos en hexadecimal
for linea in lectura.readlines():
    '''
        Aunque esta forma es lenta y riesgosa por existencia de variable copia en el tiempo, 
        es la única que encuentro para concentrar todo el contenido en una variable para
        luego cifrar.
    '''
    # Aprovecho ya para ir cifrando para lograr mas seguridad al menos en memoria
    copia += hex((linea.__hash__() - 2).__abs__())
# Ya cierro la lectura del archivo y hasheo los hashes de las lineas por seguridad en memoria
lectura.close()
del lectura
# Hago así para aumentar complejidad y asimetría del cifrado
copia = hex(copia.__hash__().__abs__() * 512).upper().replace("X", "x")
# Sobre escribo el archivo con la copia cifrada para que pierda lo anterior (debe haber copia de archivo en unidad externa por seguridad)
cifrar = open(sys.argv[1].__str__(), 'w')
# Como recibo el nombre de afuera debo transformarlo en cadena para evitar inyecciones de código por parametro mal ingresado
cifrar.write(copia + '\n')
# Cierro para evitar memory leaks y accesos no deseados por no liberar el archivo de la memoria
cifrar.close()
# Ya no necesito la referencia al archivo así que la elimino de la memoria por seguridad
del cifrar
# Muestro que el archivo se cifro
print(f'\n\tEl archivo "{sys.argv[1].__str__()}" ha sido cifrado con hasher:\n\n\t\t{copia.__str__()}\n')
# Ya no necesito de la copia y mósdulo sys porque mostré el resultado, los elimino de memoria
del sys, copia
