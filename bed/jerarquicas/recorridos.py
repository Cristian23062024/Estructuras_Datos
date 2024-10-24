# PRE-ORDEN
def pre_orden(arbol_bin):
    __pre_orden(arbol_bin.raiz)
    
def __pre_orden(sub_arbol):
    if sub_arbol:
        print(sub_arbol, False)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)

# CONSULTA #1
def str_pre_orden(arbol_bin, sep="|"):
    """Retorna una cadena en PRE-ORDEN, separando cada valor clave con 'sep',
    además identificar cada tipo de nodo con los siguientes emojis:
    - '[🌲]' si corresponde a la raíz del árbol
    - '(🌿)' si corresponde a un nodo rama
    - '(🍂)' si corresponde a un nodo hoja

    Ejemplo:
    
    			 ____50___ <--raiz
				/ 		  '\'
		_______40_ 		 _60_______
	   /  		  '\'     / 	       '\'
	 _30___       41   55      ____75___
    /      '\'                  /         ''\''
    25    _35                65        _86
         /                    '\'       /
        32                    68     77
        
    '[🌲]50|(🌿)40|(🌿)30|(🍂)25|(🌿)35|(🍂)32|(🍂)41|(🌿)60|(🍂)55|(🌿)75|(🌿)65|(🍂)68|(🌿)86|(🍂)77'
    """
    return sep.join(__str_pre_orden(arbol_bin.raiz, True))
    
def __str_pre_orden(nodo, es_raiz=False):
    if nodo is None:
        return []
    
    resultado = []
    if es_raiz:
        resultado.append(f"[🌲]{nodo.clave}")
    elif nodo.izq or nodo.der:
        resultado.append(f"(🌿){nodo.clave}")
    else:
        resultado.append(f"(🍂){nodo.clave}")
    
    resultado.extend(__str_pre_orden(nodo.izq, False))
    resultado.extend(__str_pre_orden(nodo.der, False))
    return resultado

    

# IN-ORDEN
# CONSULTA #2
def in_orden(arbol_bin):
    def __in_orden(nodo):
        if nodo:
            __in_orden(nodo.izq)
            print(nodo.clave, end=" ")
            __in_orden(nodo.der)
    
    __in_orden(arbol_bin.raiz)
    print()  # Para agregar un salto de línea al final

# CONSULTA #3
def str_in_orden(arbol_bin, sep=":"):
    """- '[🌲]' si corresponde a la raíz del árbol
    - '(🌿)' si corresponde a un nodo rama
    - '(🍂)' si corresponde a un nodo hoja

    Ejemplo:
    
    			 ____50___ <--raiz
				/ 		  ''\''
		_______40_ 		 _60_______
	   /  		  '\'     / 	       ''\''
	 _30___       41   55      ____75___
    /      '\'                  /         ''\''
    25    _35                65        _86
         /                    '\'       /
        32                    68     77
        
    '[🌲]50:(🌿)40:(🌿)30:(🍂)25:(🌿)35:(🍂)32:(🍂)41:(🌿)60:(🍂)55:(🌿)75:(🌿)65:(🍂)68:(🌿)86:(🍂)77'
    """
    return sep.join(__str_in_orden(arbol_bin.raiz, True))
    
def __str_in_orden(nodo, es_raiz=False):
    if nodo is None:
        return []
    
    resultado = []
    resultado.extend(__str_in_orden(nodo.izq, False))
    
    if es_raiz:
        resultado.append(f"[🌲]{nodo.clave}")
    elif nodo.izq or nodo.der:
        resultado.append(f"(🌿){nodo.clave}")
    else:
        resultado.append(f"(🍂){nodo.clave}")
    
    resultado.extend(__str_in_orden(nodo.der, False))
    return resultado



# POST-ORDEN
# CONSULTA #4
def post_orden(arbol_bin):
    def __post_orden(nodo):
        if nodo:
            __post_orden(nodo.izq)
            __post_orden(nodo.der)
            print(nodo.clave, end=" ")
    
    __post_orden(arbol_bin.raiz)
    print()  # Para agregar un salto de línea al final

# CONSULTA #5
def str_post_orden(arbol_bin, sep="^"):
    """Retorna una cadena en POST-ORDEN, separando cada valor clave con 'sep',
    además identificar cada tipo de nodo con los siguientes emojis:
    - '[🌲]' si corresponde a la raíz del árbol
    - '(🌿)' si corresponde a un nodo rama
    - '(🍂)' si corresponde a un nodo hoja

    Ejemplo:
    
    			 ____50___ <--raiz
				/ 		  '\'
		_______40_ 		 _60_______
	   /  		  '\'     / 	       '\'
	 _30___       41   55      ____75___
    /      '\'                  /         '\'
    25    _35                65        _86
         /                    '\'       /
        32                    68     77
        
    '[🌲]50^(🌿)40^(🌿)30^(🍂)25^(🌿)35^(🍂)32^(🍂)41^(🌿)60^(🍂)55^(🌿)75^(🌿)65^(🍂)68^(🌿)86^(🍂)77'
    """
    return sep.join(__str_post_orden(arbol_bin.raiz, True))
    
def __str_post_orden(nodo, es_raiz=False):
    if nodo is None:
        return []
    
    resultado = []
    resultado.extend(__str_post_orden(nodo.izq, False))
    resultado.extend(__str_post_orden(nodo.der, False))
    
    if es_raiz:
        resultado.append(f"[🌲]{nodo.clave}")
    elif nodo.izq or nodo.der:
        resultado.append(f"(🌿){nodo.clave}")
    else:
        resultado.append(f"(🍂){nodo.clave}")
    
    return resultado


