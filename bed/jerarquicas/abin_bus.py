from bed.jerarquicas.abin import ArbolBin
from bed.jerarquicas.excepciones import DuplicateKeyError
from bed.jerarquicas.nodos import NodoArbol_Bin


class ArbolBinario_Bus(ArbolBin):

    def adicionar(self, nueva_clave):
        self.raiz = self.__adicionar(self.raiz, nueva_clave)

    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif nueva_clave < sub_arbol.clave:  # Por izquierda
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave:  # Por derecha
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        else:
            raise DuplicateKeyError
        return sub_arbol

    def encontrar(self, clave_encotrar):
        return self.__encontrar(self.raiz, clave_encotrar)

    def __encontrar(self, sub_arbol, clave_encotrar):
        if sub_arbol.clave == clave_encotrar:
            return sub_arbol.clave
        elif clave_encotrar < sub_arbol.clave:
            return self.__encontrar(sub_arbol.izq, clave_encotrar)
        else:
            return self.__encontrar(sub_arbol.der, clave_encotrar)
        return None

    def remover(self, clave_remover, mayor=True):
        pass
