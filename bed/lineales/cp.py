# Cristian Camilo Montenegro Basante
# Edgar Chaux

from bed.lineales.cola import Cola
from bed.lineales.nodos import NodoPrioridad

class ColaPrioridad: #Con Colas
    """Clase que implementa el funcionamiento del TAD Cola de
    Prioridad, utilizando varias Colas, según el número de
    prioridades existentes. Serán atendidos, o tienen MAYOR
    prioridad, los Nodos que se encuentren en las Colas que
    manejen un valor de prioridad menor.
    """
    
    def __init__(self):
        """Metodo constructor de una cola de prioridad con varias colas
        """
        self.items = []
        self.tipo = None

    def es_vacia(self):
        """Metodo que verifica si la cola es vacia o no

        Returns
        -------
        bool
            True en caso de que este vacia y False cuando no lo es
        """
        return len(self.items) == 0
    
    def encolar(self, nuevo_dato, prioridad):
        """Método que adiciona un nuevo dato a la Cola correspondiente, según
        la prioridad que éste tendrá.

        Parameters
        ----------
        nuevo_dato : Object
            Dato que se agregará a la cola de prioridad
        prioridad : int
            Prioridad del dato a agregar

        Returns
        -------
        bool
            True en caso de poder encolar, False caso contrario
        """
        if self.es_vacia():
            self.tipo = type(nuevo_dato)
        elif not isinstance(nuevo_dato, self.tipo):
            return False

        for i, (p, cola) in enumerate(self.items):
            if p == prioridad:
                cola.encolar(nuevo_dato)
                return True
            elif p > prioridad:
                nueva_cola = Cola()
                nueva_cola.encolar(nuevo_dato)
                self.items.insert(i, (prioridad, nueva_cola))
                return True

        nueva_cola = Cola()
        nueva_cola.encolar(nuevo_dato)
        self.items.append((prioridad, nueva_cola))
        return True
    
    def desencolar(self):
        """Metodo que saca el primer dato de la cola de mayor prioridad

        Returns
        -------
        Object
            Retorna el dato que se quito de la cola
        """
        if self.es_vacia():
            return None
        prioridad, cola = self.items[0]
        elemento = cola.desencolar()
        if cola.es_vacia():
            self.items.pop(0)
        return elemento
    
    def frente(self):
        """Metodo que retorna el primer dato de mayor prioridad

        Returns
        -------
        Object
            Retorna el dato que esta al frente de la cola de mayor prioridad
        """
        if self.es_vacia():
            return None
        return self.items[0][1].frente()
    
    def __len__(self):
        """Metodo que retorna el tamaño de la cola

        Returns
        -------
        int
            Retorna el numero de colas que hay (prioridades)
        """
        return len(self.items)
    
    def __str__(self):
        """Metodo que permite imprimir las colas de prioridad

        Returns
        -------
        str
            Retorna una cadena de texto con todas las colas
        """
        if self.es_vacia():
            return "@|"
        
        resultado = "@|"
        for prioridad, cola in self.items:
            elementos_cola = ", ".join(str(elem) for elem in cola.items)
            resultado += f"<-{{P{prioridad}: [{elementos_cola}]}}"
        
        return resultado

# class ColaPrioridad: #Con Nodos
    
#     def __init__(self):
#         self.items = []
#         self.tipo = None

#     def es_vacia(self):
#         return len(self.items) == 0
    
#     def encolar(self, nuevo_dato, prioridad):
#         nuevo_nodo = NodoPrioridad(nuevo_dato, prioridad)
        
#         if self.es_vacia():
#             self.tipo = type(nuevo_dato)
#             self.items.append(nuevo_nodo)
#             return True
#         else:
#             if isinstance(nuevo_dato, self.tipo):
#                 self.items.append(nuevo_nodo)
#                 self.items.sort(key=self.__sort)
#                 return True
        
#         return False

    
#     def desencolar(self):
#         if self.es_vacia():
#             return None
#         return self.items.pop(0)
    
#     def frente(self):
#         if self.es_vacia():
#             return None
#         return self.items[0]
    
#     def __len__(self):
#         return len(self.items)
    
#     def __str__(self):
#         if self.es_vacia():
#             return "@|"
#         elif len(self) == 1:
#             return f"@|<-{{{self.items[0]}}}"
#         else:
#             return "@|<-{" + "}<-[".join(str(item) for item in self.items) + "]"
        
#     def __sort(self, nuevo_nodo):
#         return nuevo_nodo.prioridad
        