#!/usr/bin/python3
# Importo modulo para leer comandos
import sys
# Importo módulo a realizar pruebas
import hashy

# Uso formato nuevo de hasher con argumentos multilpes: ./hashy_test.py hash_1 hash_2 hash_n
for hash_n in range(1, int(sys.argv.__len__())):
    # Pruebo archivo valido
    if hashy.archivo_valido(hash_n, 'resultado_4.txt'):
        print(f'\nEl hash "{sys.argv[int(hash_n)].__str__()}" es valido para "resultado_4.txt".\n')
    else:
        print(f'\nEl hash "{sys.argv[int(hash_n)].__str__()}" no verifica para "resultado_4.txt".\n')
    # Pruebo lista valida
    if hashy.lista_valida(hash_n, [1, 3, 5]):
        # Pruebo hash de lista
        print(f'\n\nLa lista [1, 3, 5] es valida y tiene hash: {hahsy.hash_lista([1, 2, 3]).__str__()}.\n')
    else:
        print('La lista [1, 3, 5] no coincide con el hash.\n')
    # Muestro ejemplos de algunos hash de archivo
    for identificador in range(1, 7):
        print(f'\tEl archivo "test_{identificador.__str__()}.txt" tiene hash %s\n' % hashy.hash_archivo(f'test_{identificador.__str__()}.txt').__str__())
    # Elimino lo que no necesito de memoria por seguridad
del sys, hashy
