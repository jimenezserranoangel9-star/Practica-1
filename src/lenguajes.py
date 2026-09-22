# src/lenguajes.py

def concatenar_cadenas(u: str, v: str) -> str:
    return u + v

def potencia_cadena(u: str, n: int) -> str:
    if n < 0:
        raise ValueError("La potencia debe ser un entero no negativo.")
    return u * n

def inversion_cadena(u: str) -> str:
    return u[::-1]

def longitud_cadena(u: str) -> int:
    return len(u)

def concatenar_lenguajes(L1: set, L2: set) -> set:
    return {u + v for u in L1 for v in L2}

def union_lenguajes(L1: set, L2: set) -> set:
    return L1.union(L2)

def interseccion_lenguajes(L1: set, L2: set) -> set:
    return L1.intersection(L2)

def diferencia_lenguajes(L1: set, L2: set) -> set:
    return L1.difference(L2)

def potencia_lenguaje(L: set, n: int) -> set:
    if n == 0:
        return {""}
    resultado = L.copy()
    for _ in range(n - 1):
        resultado = concatenar_lenguajes(resultado, L)
    return resultado