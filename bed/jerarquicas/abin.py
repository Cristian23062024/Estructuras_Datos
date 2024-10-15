from bed.jerarquicas.nodos import NodoArbol_Bin
from random import random # Genera valores aleatorios entre 0 y 1.0

class ArbolBin:
    def __init__(self):
        self.raiz = None
        
    def adicionar(self, nueva_clave):
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
    
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif random() <= 0.5:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        else:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        return sub_arbol
    
    def encontrar(self, clave_encontrar):
        return self.__encontrar(self.raiz, clave_encontrar)
    
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol is not None:
            # print(f'{sub_arbol.clave} <--> {clave_encontrar}')
            # print(('O' if sub_arbol.izq else 'X') + ':' + ('O' if sub_arbol.der else 'X'))
            if sub_arbol.clave == clave_encontrar:
                return sub_arbol.clave
            else:
                clave_izq = self.__encontrar(sub_arbol.izq, clave_encontrar)
                if clave_izq == clave_encontrar:
                    return clave_izq
                clave_der = self.__encontrar(sub_arbol.der, clave_encontrar)
                if clave_der == clave_encontrar:
                    return clave_der
        return None
    
    def __len__(self):
        return self.__cantidad_nodos(self.raiz)
    
    def __cantidad_nodos(self, sub_arbol):
        if sub_arbol:
            return (1 +
                    self.__cantidad_nodos(sub_arbol.izq) +
                    self.__cantidad_nodos(sub_arbol.der))
        return 0
    
    # Tarea
    
    def hojas(self):
        return self.__cantidad_hojas(self.raiz)

    def __cantidad_hojas(self, sub_arbol):
        indice = 0
        if sub_arbol is not None:
            if sub_arbol.izq is not None or sub_arbol.der is not None:
                self.__cantidad_hojas(sub_arbol.izq)
                self.__cantidad_hojas(sub_arbol.der)
            else:
                indice += 1
        return indice
    
    def internos(self):
        return self.__cantidad_internos(self.raiz)

    def __cantidad_internos(self, sub_arbol):
        indice = 0
        if sub_arbol is not None:
            if sub_arbol.izq is not None or sub_arbol.der is not None:
                indice += 1
            else:
                self.__cantidad_internos(sub_arbol.izq)
                self.__cantidad_internos(sub_arbol.der)
        return indice

    
    def altura(self):
        pass
    
    