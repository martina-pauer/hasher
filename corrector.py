#!/usr/bin/python3

'''
    Garantiza consistencia a un archivo original de copia:

        1) Listar archivos a analizar

        2) Obtener hash de archivo original.

        3) Obtener hash de cada archivo listado, si no
           coincide con hash de archivo original, copiarle
           contenido original
'''
import hashy, sys

archivos = ['a.txt', 'b.txt', 'c.txt']
# Recibe de parametro el nombre o ruta completa al archivo original
for archivo in archivos:
    if not hashy.archivo_valido(hashy.hash_archivo(sys.argv[1]), archivo):
        print(f'\n\tContenido de archivo original copiado a "{archivo}"\n')
        # Copio contenido de original a nuevo desde aqui por razones de seguridad y encapsulamiento
        referencia_primera = open(sys.argv[1], 'r')
        # Para optimizar uso de interprete que va de linea a linea pongo mas lineas de código útil
        referencia_segunda = open(archivo, 'w')
        for linea in referencia_primera.readlines():
            referencia_segunda.write(linea)
        # Cierro todo por seguridad en memoria y limpo variables
        referencia_segunda.close()
        referencia_primera.close()
        del referencia_segunda, referencia_primera
    else:
        print(f'\n\tArchivo "{archivo}" es copia del original\n')
# Elimino lo que no necesito de memoria
del sys, archivos, hashy
