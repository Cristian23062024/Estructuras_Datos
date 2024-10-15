from bed.lineales.nodos import Nodo_listaSE

class Lista_SE:
    """Clase que implementa una lista simplemente enlazada
    """
    def __init__(self):
        """Metodo constructor de una lista simplemente enlazada
        """
        self.__cab = None
    
    def __str__(self):
        actual = self.__cab
        cad = ''
        while actual != None:
            cad += str(actual) + ' :>: '
            actual = actual.sig
        return cad
            
    
    def es_vacia(self):
        """Metodo que analiza si la lista esta vacia

        Returns
        -------
        bool
            retorna true si la lista esta vacia y caso contrario false
        """
        return self.__cab is None
        
        # if self.__cab:
        #     return False
        # return True
        
        # if self.__cab is None:
        #     return True
        # return False
        
        # if self.__cab is None:
        #     return True
        # else:
        #     return False
        
    def adicionar(self, nuevo_dato):
        """Metodo que permite agregar nodos a la lista

        Parameters
        ----------
        nuevo_dato : object
            Dato necesario para crear el nodo

        Returns
        -------
        bool
            Retorna True si el dato es del mismo tipo que los nodos de la
            lista y False si no es del mismo tipo
        """
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
            
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            # La lista ya tiene almenos un nodo
            actual = self.__cab
            if isinstance(nuevo_dato, type(actual.dato)):
                while actual.sig is not None:
                    actual = actual.sig
                actual.sig = nuevo_nodo
            else:
                print(f'{nuevo_dato} no se agrego porque no es del tipo de la lista')
            return isinstance(nuevo_dato, type(actual.dato))
                
    def posicionar(self, nuevo_dato, pos):
        actual = self.__cab
        indice = 0
        nodo = Nodo_listaSE(nuevo_dato)
        anterior = None
        
        if self.__len__() <= int(pos):
            if self.es_vacia():
                print('Unica posicion disponible 0')
            else:
                while indice != pos and actual:
                    anterior = actual
                    actual = actual.sig
                    indice += 1
                anterior.sig = nodo
                nodo.sig = actual
        else:
            print('posicion no valida')
                
            
                
    def recorrer(self):
        """Metodo que recorre la lista e imprime los datos dentro de esta
        """
        actual = self.__cab
        while actual:
            print(actual)
            actual = actual.sig
            
    def encontrar(self, dato_encontrar):
        """Metodo que permite encontrar datos dentro de la lista

        Parameters
        ----------
        dato_encontrar : object
            Dato a buscar en la lista

        Returns
        -------
        object | None
            retorna el dato encontrado o en caso de no encontrarlo retorna None
        """
        actual = self.__cab
        
        # while actual:
        #     if actual.dato == dato_encontrar:
        #         return actual.dato
        #     actual = actual.sig
        # return None
        
        while actual and actual.dato != dato_encontrar:
            actual=actual.sig
        return actual.dato if actual else None
    
    def remover(self, item, por_pos=True):
        if por_pos:
            return self.__remover_pos(item)
        else:
            return self.__remover_dato(item)
            
    def __remover_pos(self, pos_elm):
        actual = self.__cab
        indice = 0
        anterior = None
        
        if pos_elm >= 0:
            while actual and indice < pos_elm:
                anterior = actual
                actual = actual.sig
                indice += 1
            if indice == 0 and actual:
                self.__cab = actual.sig
            elif actual:
                anterior.sig = actual.sig
        
        return True if actual and pos_elm == indice else False
    
                    
    def __remover_dato(self, dato_elm):
        actual = self.__cab
        anterior = None
        if self.es_vacia():
            print('Lista Vacia')
        else:
            while actual and actual.dato != dato_elm:
                anterior = actual
                actual = actual.sig
            if actual:
                anterior.sig = actual.sig
            else:
                anterior.sig = actual

        return True if actual else False
    
    def ubicar(self, pos):
        actual = self.__cab
        indice = 0
        
        while actual and indice != pos:
            actual = actual.sig
            indice += 1
            
        return actual if actual else None
    
    def __len__(self):
        actual = self.__cab
        indice = 0
        
        while actual:
            actual = actual.sig
            indice += 1
            
        return indice
    
    def __iter__(self):
        self.actual1 = self.__cab
        return self
        
    def __next__(self):
        x = self.actual1
        if self.actual1:
            self.actual1 = self.actual1.sig
        else:
            raise StopIteration
            
        return x
        
        
        