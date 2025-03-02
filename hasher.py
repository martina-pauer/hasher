#!/usr/bin/python3

# Compila a su hash s2hp512h un documento que reciba como parametros en hashes hexadecimales

import sys, hashy
# Argumento Multiple en comandos ./hasher.py arch_1 arch_2 arch_3 arch_n
for archivo_n in range(1, int(sys.argv.__len__())):
# Hago uso de hashy para obtener un hash mas consistente y hacer uso de un módulo reutilizable para estandarizar 
    copia = hashy.hash_archivo(sys.argv[int(archivo_n.__str__())]).upper().replace("X", "x")
# Sobre escribo el archivo con la copia cifrada para que pierda lo anterior (debe haber copia de archivo en unidad externa por seguridad)
    hashing = open(sys.argv[int(archivo_n)].__str__(), 'w')
# Como recibo el nombre de afuera debo transformarlo en cadena para evitar inyecciones de código por parametro mal ingresado
    hashing.write(copia.__str__() + '\n')
# Cierro para evitar memory leaks y accesos no deseados por no liberar el archivo de la memoria
    hashing.close()
# Ya no necesito la referencia al archivo así que la elimino de la memoria por seguridad
    del hashing
# Muestro que el archivo se transformo en su hash
    print(f'\n\tEl archivo "{sys.argv[int(archivo_n)].__str__()}" ha sido compilado a su hash con hasher:\n\n\t\t{copia.__str__()}\n')
# Ya no necesito de la copia y mósdulo sys porque mostré el resultado, los elimino de memoria
    del copia
# Cierro después de compilar a su hash todos los archivos pasados por parametro por que lo necesito dentro del ciclo
del sys
