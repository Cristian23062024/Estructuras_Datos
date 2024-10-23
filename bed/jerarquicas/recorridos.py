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
    - '[ ]' si corresponde a la raíz del árbol🌲
    - '( )' si corresponde a un nodo rama🌿
    - '( )' si corresponde a un nodo hoja🍂
    Ejemplo:
    ____50___ <--raiz
    / \
    _______40 _60______
    / \ / \
    _30___ 41 55 ____75___
    / \ / \
    25 _35 65 _86
    / \ /
    32 68 77
    '[ ]50|( )40|( )30|( )25|( )35|( )32|( )41|( )60|( )55|( )75|( )65|( )68|( )86|( )77'🌲 🌿 🌿 🍂 🌿 🍂 🍂 🌿 🍂 🌿 🌿 🍂 🌿 🍂
    """
    pass
# IN-ORDEN
# CONSULTA #2
def in_orden(arbol_bin):
    pass
# CONSULTA #3
def str_in_orden(arbol_bin, sep=":"):
    """Retorna una cadena en IN-ORDEN, separando cada valor clave con 'sep',
    además identificar cada tipo de nodo con los siguientes emojis:
    - '[ ]' si corresponde a la raíz del árbol🌲
    - '( )' si corresponde a un nodo rama🌿
    - '( )' si corresponde a un nodo hoja🍂
    Ejemplo:
    ____50___ <--raiz
    / \
    _______40 _60______
    / \ / \
    _30___ 41 55 ____75___
    / \ / \
    25 _35 65 _86
    / \ /
    32 68 77
    '( )25:( )30:( )32:( )35:( )40:( )41:[ ]50:( )55:( )60:( )65:( )68:( )75:( )77:( )86'🍂 🌿 🍂 🌿 🌿 🍂 🌲 🍂 🌿 🌿 🍂 🌿 🍂 🌿
    """
    pass
# POST-ORDEN
# CONSULTA #4
def post_orden(arbol_bin):
    pass
# CONSULTA #5
def str_post_orden(arbol_bin, sep="^"):
    """Retorna una cadena en POST-ORDEN, separando cada valor clave con 'sep',
    además identificar cada tipo de nodo con los siguientes emojis:
    - '[ ]' si corresponde a la raíz del árbol🌲
    - '( )' si corresponde a un nodo rama🌿
    - '( )' si corresponde a un nodo hoja🍂
    Ejemplo:
    ____50___ <--raiz
    / \
    _______40 _60______
    / \ / \
    _30___ 41 55 ____75___
    / \ / \
    25 _35 65 _86
    / \ /
    32 68 77
    '( )25^( )32^( )35^( )30^( )41^( )40^( )55^( )68^( )65^( )77^( )86^( )75^( )60^[ ]50'🍂 🍂 🌿 🌿 🍂 🌿 🍂 🍂 🌿 🍂 🌿 🌿 🌿 🌲
    """
    pass