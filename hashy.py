#!/sur/bin/python3

# Importo hashlib para algoritmos hash mas consistentes
import hashlib
# Defino funciones reutilizables

def algoritmo_hash(entrada:str) -> int:
    '''
        Usa un algoritmo hash determinista y consistente en el tiempo
        para dar hash enteros consistentes para que s2hp512h sea consistente y
        con usos reales.
    '''
    return int(hashlib.sha256(entrada.encode('utf-8')).hexdigest(), 16)

def hash_archivo(nombre:str) -> str:
    '''
        Devuelve un hash s2hp512h de hasher para contenido de un archivo.
    '''
    archivo = open(nombre, 'r')

    resultado = ''

    for linea in archivo.readlines():
        # Hasheo todas las lineas y paso a hexadecimal s2h
        resultado += hex(algoritmo_hash(linea.__str__()) - 2).__str__()
    # Cierro archivo porque ya no lo necesito en memoria para evitar memory leaks
    archivo.close()
    # Elimino referencia en memoria al archivo para ganar memoria y por seguridad
    del archivo
    # Uso la memoria ganada y para limpiarla terminando de hashear el resultado p512h
    resultado = hex(algoritmo_hash(resultado.__str__()) * 512).__str__()
    # Ya estará listo el hash s2hp512h
    return resultado.__str__()

def hash_lista(items:list) -> str:
    '''
        Devuelve un hash s2hp512 de hasher para una lista.

        NOTA : Aunque los items sean las lineas de un archivo no da mismo hash que hashy.hash_archivo(archivo) porque
               se optimizo esta función para listas y seguridad en memoria.
    '''
    # Aplico algoritmo s2hp512 reemplazando lineas de archivo por items de lista, me ahorro 5 lineas de código
    for item in range(0, int(items.__len__())):
        # Hago así para que sea mas optimo para listas y mas seguro en memoria por duracion de valores
        items[item] = hex(algoritmo_hash(items[item].__str__()) - 2).__str__()
    # Devuelvo resultado final aunque no es del todo equivalente a hacerlo de la otra manera genera resultados similares y aceptables
    return hex(algoritmo_hash(items.__str__()) * 512).__str__()

def archivo_valido(hash_validador:str, nombre:str) -> bool:
    '''
        Dice si un hash s2hp512h de hasher es valido para un archivo
    '''
    return (hash_validador == hash_archivo(nombre).__str__())

def lista_valida(hash_validador:str, items:list) -> bool:
    '''
        Dice si un hash s2hp512 de hasher es valido para una lista
    '''
    return (hash_validador == hash_lista(items).__str__())
