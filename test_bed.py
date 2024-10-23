from bed.jerarquicas.abin_bus import ArbolBinario_Bus
from bed.jerarquicas.recorridos import str_in_orden
from persona import Persona

    
def test_numeros():
    lst_num = [20, 5, 35, 28, 15, 7]
    abb_num = ArbolBinario_Bus()
    for num in lst_num:
        abb_num.adicionar(num)
        
    num_enc = int(input('Ecriba el numero a encontrar:'))
    print(f'El numero {num_enc}' +
          (' No existe' if abb_num.encontrar(num_enc) is None else ' Si existe'))
    
def test_personas():
    p1 = Persona("Lizett", 20)
    p2 = Persona("Pablo", 21)
    p3 = Persona("Pedro", 23)
    p4 = Persona("Camilo", 24)
    p5 = Persona("UWU", 27)
    
    abb_per = ArbolBinario_Bus()
    
    abb_per.adicionar(p1)
    abb_per.adicionar(p2)
    abb_per.adicionar(p3)
    abb_per.adicionar(p4)
    abb_per.adicionar(p5)


if __name__ == "__main__":
    test_personas()
    # Consultar como ana,21 y ana,50 puedan convivir en el mismo arbol