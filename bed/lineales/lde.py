# CRISTIAN CAMILO MONTENEGRO BASANTE
# MARITZA FERNANDA VALENCIA

from bed.lineales.nodos import Nodo_ListaDE

class Lista_DE:
    """clase de lista do
    """
    def __init__(self):
        self.__cab = None
        self.__fin = None
        
    @property
    def inverso(self):
        self.__invertir()
        return self
    
    def __invertir(self):
        actual = self.__cab
        while actual:
            actual.sig, actual.ant = actual.ant, actual.sig
            actual = actual.ant
        self.__cab, self.__fin = self.__fin, self.__cab

    
    def es_vacia(self):
        return self.__cab is None
    
    def adicionar(self, nuevo_dato):
        nuevo_nodo = Nodo_ListaDE(nuevo_dato)
        actual = self.__cab
        if self.es_vacia():
            self.__cab = nuevo_nodo
            self.__fin = nuevo_nodo
        else:
            if isinstance(nuevo_dato, type(actual.dato)):
                while actual.sig is not None:
                    actual = actual.sig
                actual.sig = nuevo_nodo
                actual.sig.ant = actual
                self.__fin = nuevo_nodo
            else:
                print(f'{nuevo_dato} no se agrego por ser diferente tipo de la lista')
                return False
        return True
                
    
    def posicionar(self, nuevo_dato, pos=0):
        
        nuevo_nodo = Nodo_ListaDE(nuevo_dato)


        if self.es_vacia() and pos == 0:
            self.__cab = nuevo_nodo
            self.__fin = nuevo_nodo
            return True

        elif pos == 0:
            nuevo_nodo.sig = self.__cab
            self.__cab.anterior = nuevo_nodo
            self.__cab = nuevo_nodo
            return True
                
        actual = self.__cab
        i = 0

        while actual is not None and i < pos - 1:
            actual = actual.sig
            i += 1

        if actual is None:  
            return False

        nuevo_nodo.sig = actual.sig
        nuevo_nodo.ant = actual
        if actual.sig:
            actual.sig.ant = nuevo_nodo
        actual.sig = nuevo_nodo

        if nuevo_nodo.sig is None:  
            self.__fin = nuevo_nodo
        return True
    
    def remover(self, item, por_pos=True):
        if por_pos:
            return self.__remover_por_posicion(item)
        else:
            return self.__remover_por_dato(item)

    def __remover_por_posicion(self, pos):
        if self.es_vacia() or pos < 0:
            return False

        if pos == 0:
            self.__cab = self.__cab.sig
            if self.__cab:
                self.__cab.ant = None
            else:
                self.__fin = None
            return True

        actual = self.__cab
        for _ in range(pos):
            if actual is None:
                return False
            actual = actual.sig

        if actual is None:
            return False

        if actual.ant:
            actual.ant.sig = actual.sig
        if actual.sig:
            actual.sig.ant = actual.ant
        if actual == self.__fin:
            self.__fin = actual.ant

        return True

    def __remover_por_dato(self, dato):
        if self.es_vacia():
            return False

        removido = False
        actual = self.__cab
        while actual:
            if actual.dato == dato:
                if actual == self.__cab:
                    self.__cab = actual.sig
                    if self.__cab:
                        self.__cab.ant = None
                else:
                    actual.ant.sig = actual.sig

                if actual == self.__fin:
                    self.__fin = actual.ant
                elif actual.sig:
                    actual.sig.ant = actual.ant

                siguiente = actual.sig
                actual = siguiente
                removido = True
            else:
                actual = actual.sig

        return removido
    
    def encontrar(self, dato_buscar):
        actual = self.__cab
        while actual and dato_buscar != actual.dato:
            actual = actual.sig
        return actual if actual else None
    
    def ubicar(self, pos):
        actual = self.__cab
        index = 0
        while index != pos and actual:
            actual = actual.sig
            index+=1
        return actual if actual else None
    
    def adelante(self):
        actual = self.__cab
        if actual is None:
            print("La lista está vacía.")
            return

        while actual is not None:
            print(actual.dato)
            actual = actual.sig
            
    
    def atras(self):
        actual = self.__fin
        if actual is None:
            print("La lista está vacía.")
            return

        while actual is not None:
            print(actual.dato)
            actual = actual.ant
    
    def __str__(self):
        if self.es_vacia():
            return ""
        actual = self.__cab
        resultado = ""
        while actual:
            resultado += str(actual.dato)
            if actual.sig:
                resultado += " <=> "
            actual = actual.sig
        return resultado
        
    
    def __len__(self):
        actual = self.__cab
        indice = 0
        while actual:
            actual=actual.sig
            indice+=1
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