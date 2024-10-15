class Nodo_listaSE():
    """Clase que modela un nodo para el tipo de estructura lista simplemente
    enlazada.
    """
    
    def __init__(self, dato):
        """Método constructor de un nodo para una lista simplemente enlazada

        Parameters
        ----------
        dato : object
            El dato que se pasa al nodo
        """            
        self.dato = dato
        self.sig = None
       
    def __str__ (self):
        """Método que retorna una cadena con el dato del nodo.

        Returns
        -------
        srt
            La cadena a ser retornada por el nodo que incluye el dato.
        """
        return f'{self.dato}'
    
class Nodo_ListaDE():
    
    def __init__(self, dato):
        self.ant = None
        self.dato = dato
        self.sig = None
        
    def __str__(self):
        return f'{self.dato}'
    
class NodoPrioridad():
    """Clase de nodo con prioridad
    """
    
    def __init__(self, dato, prioridad):
        """Metodo constructor del nodo

        Parameters
        ----------
        dato : object
            Se ingresa el dato a guardar en el nodo
        prioridad : int
            Se ingresa la prioridad del nodo
        """
        self.dato = dato
        self.prioridad = prioridad
        
    def __str__(self):
        """Metodo especial str para imprimir el nodo

        Returns
        -------
        str
            retorna la cadena de texto con el dato y la prioridad de manera "dato | prioridad"
        """
        return f'{self.dato}'