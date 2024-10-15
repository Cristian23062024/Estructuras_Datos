def pre_orden(arbol_binario):
    __pre_orden(arbol_binario.raiz)

def __pre_orden(sub_arbol):
    if sub_arbol:
        print(sub_arbol)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)