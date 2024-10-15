from bed.jerarquicas.abin import ArbolBin
from bed.jerarquicas.nodos import NodoArbol_Bin


class ArbolBinario_Bus (ArbolBin):

    def adicionar(self, nueva_clave):
        self.raiz = self.__adicionar(self.raiz, nueva_clave)

    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif nueva_clave < sub_arbol.clave: # Por izquierda
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave: # Por derecha
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)

        return sub_arbol