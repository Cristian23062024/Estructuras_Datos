from bed.jerarquicas.abin import ArbolBin
from bed.jerarquicas.abin_bus import ArbolBinario_Bus
from bed.jerarquicas.nodos import NodoArbol_Bin

if __name__ == "__main__":
    arbol = ArbolBin()
    # arbol = ArbolBinario_Bus()
    
    arbol.adicionar(4)
    arbol.adicionar(5)
    arbol.adicionar(8)
    arbol.adicionar(9)
    arbol.adicionar(10)
    arbol.adicionar(14)
    arbol.adicionar(12)
    arbol.adicionar(20)
    arbol.adicionar(24)
    arbol.adicionar(23)
    arbol.adicionar(2)

    print(arbol)
