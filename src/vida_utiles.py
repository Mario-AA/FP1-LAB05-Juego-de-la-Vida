import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    tablero = []
    for f in range(filas):
        fila=[]
        for colum in range(columnas):
            fila.append(False)
        tablero.append(fila)
    return tablero

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    rndtab = []
    for f in range(filas):
        fila = []
        for colum in range(columnas):
            if random.random()< probabilidad_vida:
                fila.append(True)
            else:
                fila.append(False)
        rndtab.append(fila)
    return rndtab

def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """
    for f in range(len(tablero)):
        if f == pos_fila:
            for i in range(len(tablero[f])):#Recorrer en el tamaño de la fila del patrón
                if i == pos_col:
                    for k in range(len(patron)):#vertical,patrón
                        for m in range(len(patron[k])):#horizontal,patrón
                            tablero[f+k][i+m] = patron[k][m]
    return tablero
def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    num_vivos = 0
    for i in range (-1,2):
        for j in range(-1,2):
            if not(i == 0 and j == 0):
                f = i+fila
                c = j+col
                if f >= len(tablero):
                    f = f%len(tablero)
                if c >= len(tablero[0]):
                    c = c%len(tablero[0])
                if tablero[f][c] == True:
                    num_vivos +=1
    return num_vivos
def calcular_siguiente_generacion(tablero) -> list[list[bool]]:
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    res = crear_tablero(len(tablero),len(tablero[0]))
    for f in range(len(tablero)):
        for c in range(len(tablero[f])):
            vecinos= contar_vecinos(tablero,f,c)
            if tablero[f][c] == True:
                if vecinos == 2 or vecinos == 3:
                    res[f][c] = True
                else:
                    res[f][c] = False
            else:
                if vecinos == 3:
                    res[f][c] = True
                else:
                    res[f][c] = False
    return res
