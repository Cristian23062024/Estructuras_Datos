class Cola:
    """Clase que implementa el funcionamiento del TAD Cola
    """
    def __init__(self):
        """Método que realiza la creación e inicialización de la Cola
        """
        self.items = []
        self.tipo = None

    def es_vacia(self):
        """Metodo que verifica si la cola es vacia

        Returns
        -------
        bool
            Retorna True si la cola es vacia. False en caso contrario
        """
        return len(self.items) == 0

    def encolar(self, nuevo_dato):
        """Método que adiciona un nuevo dato al final de la cola. Realizar la
        validación de Homogeneidad para cada dato ingresado a la cola
        
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la cola
        
        Returns
        -------
        bool
        True si nuevo_dato fue encolado. False en caso contrario
        """
        if self.es_vacia():
            self.tipo = type(nuevo_dato)
            self.items.append(nuevo_dato)
            return True
        elif isinstance(nuevo_dato, self.tipo):
            self.items.append(nuevo_dato)
            return True
        return False

    def desencolar(self):
        """Método que saca/quita el primer nodo (elimina el nodo) de la cola
        y retorna su dato
        
        Returns
        -------
        object|None
        El dato del primer nodo de la cola y None cuando la cola no
        contenga nodos/datos
        """
        if self.es_vacia():
            return None
        return self.items.pop(0)

    def frente(self):
        """Método que retorna el dato del primer nodo de la cola, sin quitarlo
        de la misma
        
        Returns
        -------
        object|None
        El dato del primer nodo en la cola y None cuando la cola no
        contenga nodos/datos"""
        if self.es_vacia():
            return None
        return self.items[0]

    def __len__(self):
        """Método que retorna del número de nodos que contiene la cola
        
        Returns
        -------
        int
        Tamaño de la cola
        """
        return len(self.items)

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la cola
        
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la cola, en el siguiente formato:
        “@|<-{dato }<-[dato ]<-[dato ]<-[dato_n]” ₁ ₂ ₃
        Cuando hay un sólo dato:
        “@|<-{dato }” ₁
        Cuando no hay datos:
        “@|”
        """
        if self.es_vacia():
            return "@|"
        elif len(self) == 1:
            return f"@|<-{{{self.items[0]}}}"
        else:
            return "@|<-{" + "}<-[".join(str(item) for item in self.items) + "]"