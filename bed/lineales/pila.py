from bed.lineales.nodos import Nodo_listaSE
class Pila:
    """Clase que implementa el funcionamiento del TAD Pila
    """
    def __init__(self):
        """Método constructor que realiza la creación e inicialización de
        una Pila
        """
        self.__cab = None
        self.__tamaño = 0
        
    def es_vacia(self):
        """Método que verifica si la pila se encuentra vacía
        Returns
        -------
        bool
        Retorna True si la pila es vacia. False en caso contrario
        """
        return self.__cab is None
    
    def apilar(self, nuevo_dato):
        """Método que realiza la entrada de un nuevo dato a la pila.
        Realizar la validación de Homogeneidad para cada dato ingresado
        a la pila
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la pila
        Returns
        -------
        bool
        True si nuevo_dato fue apilado. False en caso contrario
        """
        if self.__cab is None or isinstance(nuevo_dato, type(self.__cab.dato)):
            nuevo_nodo = Nodo_listaSE(nuevo_dato)
            nuevo_nodo.siguiente = self.__cab
            self.__cab = nuevo_nodo
            self.__tamaño += 1
            return True
        return False
    
    def desapilar(self):
        """Método que saca/quita el último nodo (elimina el nodo) de la pila
        y retorna su dato
        Returns
        -------
        object|None
        El dato del nodo desapilado y None cuando la pila no contenga
        nodos/datos
        """
        if self.__cab is None:
            return None
        dato = self.__cab.dato
        self.__cab = self.__cab.siguiente
        self.__tamaño -= 1
        return dato

    def cima(self):
        """Método que retorna el dato del último nodo ingresado en la pila,
        sin quitarlo de la misma
        Returns
        -------
        object|None
        El dato del último nodo ingresado y None cuando la pila no
        contenga nodos/datos
        """
        return self.__cab.dato if self.__cab else None

    def __len__(self):
        """Método que retorna el número de nodos que contiene la pila
        Returns
        -------
        int
        __tamaño de la pila
        """
        return self.__tamaño

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la pila (sin desapilarlos)
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la pila, en el siguiente formato:
        “===(c)===
        (*[dato_n]*)
        ::
        (dato )₃
        ::
        (dato )₂
        ::
        (dato )”₁
        Cuando hay un sólo dato:
        “===(c)===
        (*[dato_n]*)”
        Cuando no hay datos:
        “===(c)===”
        """
        if self.__cab is None:
            return "===(c)==="
        
        resultado = "===(c)===\n"
        nodo_actual = self.__cab
        elementos = []
        
        while nodo_actual:
            elementos.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.siguiente
        
        if len(elementos) == 1:
            resultado += f"(*[{elementos[0]}]*)"
        else:
            resultado += f"(*[{elementos[0]}]*)"
            for i, elemento in enumerate(elementos[1:], start=1):
                subindice = ''.join([chr(8320 + int(d)) for d in str(len(elementos) - i)])
                resultado += f"\n::\n({elemento}) {subindice}"
        
        return resultado