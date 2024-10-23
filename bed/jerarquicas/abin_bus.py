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
    
    
    # CONSULTA #1
    def econtrar_minimo(self):
        """Método que busca y retorna la clave con menor valor del árbol
        binario de búsqueda, o retorna None cuando el árbol binario de
        búsqueda está vacío.
        Returns
        -------
        object|None
        object si se encuentra la clave con el menor valor del árbol
        binario de búsqueda. None en caso contrario.
        """
        pass
    
    # CONSULTA #2
    def econtrar_maximo(self):
        """Método que busca y retorna la clave con mayor valor del árbol
        binario de búsqueda, o retorna None cuando el árbol binario de
        búsqueda está vacío.
        Returns
        -------
        object|None
        object si se encuentra la clave con el mayor valor del árbol
        binario de búsqueda. None en caso contrario.
        """
        pass
    # CONSULTA #3
    def remover(self, clave_remover, mayor=True):
        """Metodo que remueve un nodo del arbol binario de busqueda

        Parameters
        ----------
        clave_remover : _type_
            _description_
        mayor : bool, optional
            _description_, by default True
        """
        pass
